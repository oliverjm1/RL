# Setting up OpenAI Gym environment etc…

## This is how I initially did it. Alternative to doing all with pip install.

# Step by step

1. Make new conda environment, with python 3.10.13: `conda create -n rl_env python=3.10.13`
1. Activate this environment: `conda activate rl_env`
1. Install mamba solver cause conda is bad: `conda install conda-libmamba-solver`
1. Install all gym stuff: `conda install -c conda-forge gym-all --solver libmamba`
1. Install torch: `pip install torch`
1. Install ipython: `pip install ipython`

## My though process as i did it at the time

*  Made new conda environment called `rl` and activated it.

*	First I tried to install by making a new conda environment and did `conda install -c conda-forge gym-all`
    *	This is taking a while. Try it but cancel if frozen on solving. Couple solving environment failed attempts on mine.
    *	Solved this problem by doing `conda install conda-libmamba-solver` and then doing 
    
    `conda install -c conda-forge gym-all --solver libmamba`
*	Installing pytorch/torchvision – again environment clashes were avoided by using the libmamba solver in conda: 

`conda install pytorch torchvision -c pytorch --solver libmamba`
*	`pip install ipython`
*	Atari games:
    *	Had to run `pip install "gym[atari, accept-rom-license]"` within rl environment.
