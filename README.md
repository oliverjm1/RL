# HACKATHON INSTRUCTIONS

### 1. Cloning This Repoository

In your terminal, navigate to where you would like to save this repository. Then do:

`git clone https://github.com/oliverjm1/RL.git`

This should create a folder called *RL*, containing the directory.

### 2. Environment Setup

The environment file can be found at the top level of this cloned repository (**rl_env.yml**).

To create an environment from this file, go to terminal, make sure you're in the directory (`cd RL`) and enter:

`conda create -f rl_env.yml` 

or maybe 

`conda env create --file rl_env.yml`

#### IF THIS DIDN'T WORK:

Hopefully this should work but it never seems to be that simple. If not, have a look at the **alt_setting_up_env.md** file which uses conda instead of pip. 

Once the environment has been created, activate it with `conda activate rl_test` (or whatever you named the environment).

### 3. Start With Example Notebook

There is a python notebook with example code for using OpenAi gym, both for playing the games manually and for training a network through reinforcement learning to play the games. This file is found in the top level of the directory (file is called **start_here.ipynb**). I've been using VSCode but you should also be able to use jupyter notebook. Just make sure that the conda rl_test environment is activated. 

To make sure you're working within a specific conda environment in jupyter notebook, make sure the environment is active and open the notebook through the terminal using `jupyter notebook start_here.ipynb` once navigated into the *RL* folder (potentially will have to do `pip install jupyter` at this point).

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
├── __init__.py
├── alt_setting_up_env.md
├── rl_env.yml
├── src
│   ├── acrobot
│   │   ├── acrobot_manual.py
│   │   └── acrobot_train.py
│   ├── breakout
│   │   ├── breakout_manual.py
│   │   └── breakout_train.py
│   ├── carRacing
│   │   └── carRacing_manual.py
│   ├── cartPole
│   │   ├── cartPole_manual.py
│   │   ├── cartPole_train.py
│   │   └── myCartPole.py
│   └── mountainCar
│       ├── mountainCar_manual.py
│       └── mountainCar_train.py
└── start_here.ipynb
```
