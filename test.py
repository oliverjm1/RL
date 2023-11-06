import gym
from gym.utils.play import play
import pygame
import numpy as np
import time 
import random


# Make the environment
env = gym.make('HumanoidStandup-v4', render_mode='rgb_array')

# Note the observation and action space
obs_space = env.observation_space
action_space = env.action_space
print(f"The observation space: {obs_space}")
print(f"The action space: {action_space}")

# Play the game
mapping = {(pygame.K_UP,): 0.4*np.ones(17, dtype=np.float32), (pygame.K_DOWN,): -0.4*np.ones(17, dtype=np.float32), (pygame.K_LEFT,): -0.2*np.ones(17, dtype=np.float32), (pygame.K_RIGHT,): 0.2*np.ones(17, dtype=np.float32)}
play(env, keys_to_action=mapping, noop=np.zeros(17, dtype=np.float32))

# Interacting with the environment
print("Upper Bound for Env Observation", env.observation_space.high)
print("Lower Bound for Env Observation", env.observation_space.low)

# Reset environment and return initial observation of the state
obs = env.reset()
print(f"The initial observation is {obs}")

done = False

while not done:


    time.sleep(0.1)

    # Sample a random action from the entire action space
    random_action = env.action_space.sample()

    # # Take the action and get the new observation space
    new_obs, reward, done, unk, info = env.step(random_action)
    # observation of state of environment;
    # reward get from environment after executing the action that was given as the input to the step function
    # whne the epsiode has been terminated - if true may need to end simulation or reset enviorment to restart the episode
    # info - addiotional info depending on the environment - e.g. lives left
    print(f"The new observation is {new_obs}")
    print(f"The reward is {reward}")
    print(f"Done is {done}")
    print(f"Info is {info}")
    print(f"Unk is {unk}")

    env.render()

# Render the environment
#env.render()
#time.sleep(3)
env.close()