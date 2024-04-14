import math
import numpy as np
import gym.spaces
from util import common_values
from util.game_state import GameState


# Action format
# [throttle, steer, pitch, yaw, roll, jump, boost, handbrake]

class YourActionParser:

    def get_action_space(self) -> gym.spaces.Space:
        # return gym.spaces.Tuple((gym.spaces.Box(-1, 1, shape=(5,)), gym.spaces.MultiBinary(3)))
        return gym.spaces.Box(-1, 1, shape=(common_values.NUM_ACTIONS,))
    
    def parse_actions(self, actions: np.ndarray, state: GameState) -> np.ndarray:

        # Convert actions to a numpy array if it's not already one
        if not isinstance(actions, np.ndarray):
            actions = np.array(actions)
            
        actions = actions.reshape((-1, 8))

        actions[..., :5] = actions[..., :5].clip(-1, 1)
        # The final 3 actions handle are jump, boost and handbrake. They are inherently discrete so we convert them to either 0 or 1.
        actions[..., 5:] = actions[..., 5:] > 0

        return actions