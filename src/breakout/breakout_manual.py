import numpy as np
import gym
from gym.utils.play import play, PlayPlot

env = gym.make("ALE/Breakout-v5", full_action_space=False)
n_actions = env.action_space
print("num actions: ", n_actions)
# Get the number of state observations
state, info = env.reset()
print("state: ",state)
print("state shape: ",state.shape)
n_observations = len(state)
print("num obs: ", n_observations)

play(gym.make("ALE/Breakout-v5", render_mode="rgb_array"), keys_to_action={
    "s": np.array(1),
    "d": np.array(2),
    "a": np.array(3),
}, noop=np.array(0), zoom=2.5)