import sys

import gym
import numpy as np
import gym.spaces


class MyEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.action_space = gym.spaces.Discrete(4) # kick, dash, turn left, turn right


