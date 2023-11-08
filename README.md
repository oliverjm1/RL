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
├── setting_up_env.md
├── src
│   ├── acrobot
│   │   └── acrobot_manual.py
│   ├── breakout
│   │   └── breakout_manual.py
│   ├── carRacing
│   │   └── carRacing_manual.py
│   ├── cartPole
│   │   ├── cartPole_manual.py
│   │   └── cartPole_train.py
│   └── mountainCar
│       ├── mountainCar_manual.py
│       └── mountainCar_train.py
├── test.py
└── test2.py
```