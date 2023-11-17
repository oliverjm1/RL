import numpy as np
import gym
from gym.utils.play import play, PlayPlot


# Below commented out is manually playing the unedited open ai gym version
# This was difficult as there was no zero action state. Cart either moved left or right.
"""env = gym.make("CartPole-v1")
n_actions = env.action_space
print("num actions: ", n_actions)
# Get the number of state observations
state, info = env.reset()
n_observations = len(state)
print("num obs: ", n_observations)

play(gym.make("CartPole-v1", render_mode="rgb_array"), keys_to_action={
    "a": np.array(0),
    "d": np.array(1),
}, noop=np.array(0))"""

# I have edited the cartpole code to attempt to include a zero state, and increased angle of termination
from myCartPole import CartPoleEnv
env = CartPoleEnv()
n_actions = env.action_space
print("num actions: ", n_actions)
# Get the number of state observations
state, info = env.reset()
n_observations = len(state)
print("num obs: ", n_observations)

play(CartPoleEnv(render_mode="rgb_array"), keys_to_action={
    "a": np.array(2),
    "d": np.array(0),
}, noop=np.array(1))
