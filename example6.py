import os
import numpy as np
# from rlgym_tools.extra_action_parsers.lookup_act import LookupAction
from rlgym_sim.utils.gamestates import GameState
from rlgym_ppo.util import MetricsLogger


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
    from rlgym_sim.utils.state_setters import RandomState
    from rlgym_sim.utils.reward_functions import CombinedReward
    from rlgym_sim.utils.reward_functions.common_rewards import VelocityPlayerToBallReward, VelocityBallToGoalReward, FaceBallReward, EventReward
    from rlgym_sim.utils.obs_builders import DefaultObs
    from rlgym_sim.utils.terminal_conditions.common_conditions import NoTouchTimeoutCondition, GoalScoredCondition
    from rlgym_sim.utils import common_values
    # from rlgym_sim.utils.action_parsers import DiscreteAction
    # from rlgym_tools.extra_action_parsers.lookup_act import LookupAction
    from rlgym_sim.utils.action_parsers import LookupAction

    spawn_opponents = True
    team_size = 1
    game_tick_rate = 120
    tick_skip = 8
    timeout_seconds = 10
    timeout_ticks = int(round(timeout_seconds * game_tick_rate / tick_skip))

    action_parser = LookupAction()
    terminal_conditions = [NoTouchTimeoutCondition(timeout_ticks), GoalScoredCondition()]

    rewards_to_combine = (EventReward(team_goal=1.5, goal=1.5, touch=0.005, shot=0.75, demo=0.3, boost_pickup=0.1),
                          VelocityPlayerToBallReward(),
                          VelocityBallToGoalReward(),
                          FaceBallReward()
                          )
    reward_weights = (10.0, 0.1, 0.25, 0.0001)

    reward_fn = CombinedReward(reward_functions=rewards_to_combine,
                               reward_weights=reward_weights)

    obs_builder = DefaultObs(
        pos_coef=np.asarray([1 / common_values.SIDE_WALL_X, 1 / common_values.BACK_NET_Y, 1 / common_values.CEILING_Z]),
        ang_coef=1 / np.pi,
        lin_vel_coef=1 / common_values.CAR_MAX_SPEED,
        ang_vel_coef=1 / common_values.CAR_MAX_ANG_VEL)

    env = rlgym_sim.make(tick_skip=tick_skip,
                         team_size=team_size,
                         spawn_opponents=spawn_opponents,
                         terminal_conditions=terminal_conditions,
                         reward_fn=reward_fn,
                         obs_builder=obs_builder,
                         action_parser=action_parser,
                         state_setter=RandomState())

    return env

if __name__ == "__main__":
    from rlgym_ppo import Learner
    metrics_logger = ExampleLogger()

    # 42 processes
    n_proc = 42

    # educated guess - could be slightly higher or lower
    min_inference_size = max(1, int(round(n_proc * 0.9)))

    last_checkpoint_num = max(os.listdir("data/checkpoints/rlgym-ppo-run-1714162990927753600/"), key=lambda d: int(d))
    checkpoints_load_dir = "data/checkpoints/rlgym-ppo-run-1714162990927753600/" + str(last_checkpoint_num)

    learner = Learner(build_rocketsim_env,
                      n_proc=n_proc,
                      min_inference_size=min_inference_size,
                    #   render=True,
                    #   render_delay=1,
                      metrics_logger=metrics_logger,
                      ppo_batch_size=50000,
                      ts_per_iteration=50000,
                      exp_buffer_size=150000,
                      ppo_minibatch_size=50000,
                      ppo_ent_coef=0.01, #0.001
                      policy_layer_sizes=(1024, 1024, 512, 512),
                      critic_layer_sizes=(1024, 1024, 512, 512),
                      ppo_epochs=3,
                      standardize_returns=True,
                      standardize_obs=False,
                      checkpoint_load_folder=checkpoints_load_dir,
                      save_every_ts=100_000,
                      timestep_limit=50_000_000_000,
                      log_to_wandb=True)
    learner.learn()