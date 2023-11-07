# Setting up OpenAI Gym environment etc…

*	First I am trying to install by making a new conda environment and doing `conda install -c conda-forge gym-all`
    *	This is taking a while. Couple solving environment failed attempts.
    *	Solved this problem by installing conda-libmamba-solver and then adding `--solver libmamba`
*	Installing pytorch/torchvision – again environment clashes were avoided by using the libmamba solver in conda: 

`conda install pytorch torchvision -c pytorch --solver libmamba`
*	`pip install ipython`
