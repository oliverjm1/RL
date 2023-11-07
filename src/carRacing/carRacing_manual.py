import numpy as np
import gym
from gym.utils.play import play
play(gym.make("CarRacing-v2", render_mode="rgb_array"), keys_to_action={
    "w": np.array([0, 0.7, 0]),
    "a": np.array([-1, 0, 0]),
    "s": np.array([0, 0, 1]),
    "d": np.array([1, 0, 0]),
    "wa": np.array([-1, 0.7, 0]),
    "dw": np.array([1, 0.7, 0]),
    "ds": np.array([1, 0, 1]),
    "as": np.array([-1, 0, 1]),
}, noop=np.array([0,0,0]))