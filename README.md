# HACKATHON INSTRUCTIONS

### 1. Environment Setup

The environment file can be found in this repository (**rl_env.yml**).

To create an environment from this file, go to terminal and enter:

`conda create -f rl_env.yml`

Hopefully this should work but it never seems to be that simple. If not, have a look at the **alt_setting_up_env.md** file which uses conda instead of pip.

Once the environment has been created, activate it with `conda activate rl_test` (or whatever you named the environment).

### 2. Cloning This Repoository

Still in terminal, navigate to where you would like to save this folder. Then do `git clone https://github.com/oliverjm1/RL.git`.

### 3. Start With Example Notebook

There is a python notebook with example code for using OpenAi gym, both for playing the games manually and for training a network through reinforcement learning to play the games. This file is found in the *src/hackathon/* folder (file is called **start_here.ipynb**). I've been using VSCode but you should also be able to use jupyter notebook. Just make sure that the conda rl_test environment is activated. To make sure you're working within a specific conda environment in jupyter notebook, make sure the environment is active and open the notebook through the terminal using `jupyter notebook start_here.ipynb` once navigated into the *hackathon* folder.

# Reinforcement Learning

This repo will contain all things related to reinforcement learning.
Hackathon on 31/01/2024.
Up until then will be messing around and experimenting with stuff.

## File/Folder Structure

Within `src`, each game has its own folder. This may contain a version of the game able to be played manually on the keyboard (denoted with suffix _manual), as well as versions for training a network to play the game through reinforcement learning.

Layout of files seen below:

```
.
├── LICENSE
├── README.md
├── alt_setting_up_env.md
├── rl_env.yml
└── src
    ├── acrobot
    │   ├── acrobot_manual.py
    │   └── acrobot_train.py
    ├── breakout
    │   ├── breakout_manual.py
    │   └── breakout_train.py
    ├── carRacing
    │   └── carRacing_manual.py
    ├── cartPole
    │   ├── __pycache__
    │   │   └── myCartPole.cpython-310.pyc
    │   ├── cartPole_manual.py
    │   ├── cartPole_train.py
    │   └── myCartPole.py
    ├── hackathon
    │   └── start_here.ipynb
    └── mountainCar
        ├── mountainCar_manual.py
        └── mountainCar_train.py
```