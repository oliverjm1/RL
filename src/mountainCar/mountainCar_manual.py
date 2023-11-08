import numpy as np
import gym
from gym.utils.play import play, PlayPlot

env = gym.make("MountainCar-v0")
n_actions = env.action_space
print("num actions: ", n_actions)
# Get the number of state observations
state, info = env.reset()
n_observations = len(state)
print("num obs: ", n_observations)

play(gym.make("MountainCar-v0", render_mode="rgb_array"), keys_to_action={
    "a": np.array(0),
    "d": np.array(2),
}, noop=np.array(1))