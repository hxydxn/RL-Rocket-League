import numpy as np
from rlgym_sim.utils.gamestates import GameState
from rlgym.utils.reward_functions import RewardFunction
from rlgym_ppo.util import MetricsLogger
from rlgym_sim.utils import common_values
from rlgym_sim.utils.gamestates import GameState, PlayerData

BACK_NET_Y = common_values.BACK_NET_Y
BACK_WALL_Y = common_values.BACK_WALL_Y
BALL_RADIUS = common_values.BALL_RADIUS
BALL_MAX_SPEED = common_values.BALL_MAX_SPEED
ORANGE_GOAL_BACK = common_values.ORANGE_GOAL_BACK
BLUE_GOAL_BACK = common_values.BLUE_GOAL_BACK
ORANGE_TEAM = common_values.ORANGE_TEAM
BLUE_TEAM = common_values.BLUE_TEAM

class LiuDistanceBallToGoalReward(RewardFunction):
    def __init__(self, own_goal=False):
        super().__init__()
        self.own_goal = own_goal

    def reset(self, initial_state: GameState):
        pass

    def get_reward(self, player: PlayerData, state: GameState, previous_action: np.ndarray) -> float:
        if player.team_num == BLUE_TEAM and not self.own_goal \
                or player.team_num == ORANGE_TEAM and self.own_goal:
            objective = np.array(ORANGE_GOAL_BACK)
        else:
            objective = np.array(BLUE_GOAL_BACK)

        # Compensate for moving objective to back of net
        dist = np.linalg.norm(state.ball.position - objective) - (BACK_NET_Y - BACK_WALL_Y + BALL_RADIUS)
        return np.exp(-0.5 * dist / BALL_MAX_SPEED)

class ExampleLogger(MetricsLogger):
    def _collect_metrics(self, game_state: GameState) -> list:
        return [game_state.players[0].car_data.linear_velocity,
                game_state.players[0].car_data.rotation_mtx(),
                game_state.orange_score]

    def _report_metrics(self, collected_metrics, wandb_run, cumulative_timesteps):
        avg_linvel = np.zeros(3)
        for metric_array in collected_metrics:
            p0_linear_velocity = metric_array[0]
            avg_linvel += p0_linear_velocity
        avg_linvel /= len(collected_metrics)
        report = {"x_vel":avg_linvel[0],
                  "y_vel":avg_linvel[1],
                  "z_vel":avg_linvel[2],
                  "Cumulative Timesteps":cumulative_timesteps}
        wandb_run.log(report)


def build_rocketsim_env():
    import rlgym_sim
    from rlgym_sim.utils.reward_functions import CombinedReward
    from rlgym.utils.reward_functions.player_ball_rewards import FaceBallReward
    from rlgym_sim.utils.reward_functions.common_rewards import VelocityPlayerToBallReward, VelocityBallToGoalReward, \
        EventReward
    from rlgym_sim.utils.obs_builders import DefaultObs
    from rlgym_sim.utils.terminal_conditions.common_conditions import NoTouchTimeoutCondition, GoalScoredCondition
    from rlgym_sim.utils.action_parsers import ContinuousAction
    from rlgym1_assets.action_parsers.action_parsers import WandbActionParser, LookupAction
    from rlgym_sim.utils.obs_builders import AdvancedObs

    spawn_opponents = True
    team_size = 1
    game_tick_rate = 120
    tick_skip = 8
    timeout_seconds = 10
    timeout_ticks = int(round(timeout_seconds * game_tick_rate / tick_skip))

    #action_parser = ContinuousAction()
    action_parser = WandbActionParser(LookupAction())
    terminal_conditions = [NoTouchTimeoutCondition(timeout_ticks), GoalScoredCondition()]

    rewards_to_combine = (VelocityPlayerToBallReward(),
                          VelocityBallToGoalReward(),
                          EventReward(team_goal=1, concede=-1, demo=0.1, shot=0.1, save=0.1, touch=0.01),
                          LiuDistanceBallToGoalReward(own_goal=False),
                          FaceBallReward()
                          )
    reward_weights = (0.01, 0.1, 10.0, 0.1, 0.1)

    reward_fn = CombinedReward(reward_functions=rewards_to_combine,
                               reward_weights=reward_weights)

    # obs_builder = DefaultObs(
    #     pos_coef=np.asarray([1 / common_values.SIDE_WALL_X, 1 / common_values.BACK_NET_Y, 1 / common_values.CEILING_Z]),
    #     ang_coef=1 / np.pi,
    #     lin_vel_coef=1 / common_values.CAR_MAX_SPEED,
    #     ang_vel_coef=1 / common_values.CAR_MAX_ANG_VEL)
    obs_builder = AdvancedObs()
    env = rlgym_sim.make(tick_skip=tick_skip,
                         team_size=team_size,
                         spawn_opponents=spawn_opponents,
                         terminal_conditions=terminal_conditions,
                         reward_fn=reward_fn,
                         obs_builder=obs_builder,
                         action_parser=action_parser)

    return env

if __name__ == "__main__":
    from rlgym_ppo import Learner
    metrics_logger = ExampleLogger()

    # 32 processes
    n_proc = 32

    # educated guess - could be slightly higher or lower
    min_inference_size = max(1, int(round(n_proc * 0.9)))

    learner = Learner(build_rocketsim_env,
                      n_proc=n_proc,
                      min_inference_size=min_inference_size,
                      metrics_logger=metrics_logger,
                      ppo_batch_size=50000,
                      ts_per_iteration=50000,
                      exp_buffer_size=150000,
                      ppo_minibatch_size=50000,
                      ppo_ent_coef=0.001,
                      ppo_epochs=1,
                      standardize_returns=True,
                      standardize_obs=False,
                      save_every_ts=100_000,
                      timestep_limit=1_000_000_000,
                      log_to_wandb=True)
    learner.learn()