import math
import os
import pickle

import numpy as np
import torch
import torch.nn.functional as F
from torch.distributions import Categorical

from your_act import YourActionParser
import your_obs
# from discrete_policy import DiscreteFF
from continuous_policy import ContinuousPolicy
from util import common_values

# You can get the OBS size from the rlgym-ppo console print-outs when you start your bot
OBS_SIZE = 89

# If you haven't set these, they are [256, 256, 256] by default
POLICY_LAYER_SIZES = [256, 256, 256]

class Agent:
	def __init__(self):
		self.action_parser = YourActionParser()
		self.num_actions = common_values.NUM_ACTIONS
		cur_dir = os.path.dirname(os.path.realpath(__file__))
		
		device = torch.device("cpu")
		self.policy = ContinuousPolicy(OBS_SIZE, self.num_actions * 2, POLICY_LAYER_SIZES, device)
		self.policy.load_state_dict(torch.load(os.path.join(cur_dir, "PPO_POLICY.pt"), map_location=device))
		torch.set_num_threads(1)

	def act(self, state):
		with torch.no_grad():
			action_idx, probs = self.policy.get_action(state, True)
		
		return self.action_parser.parse_actions([action_idx], None)[0]
