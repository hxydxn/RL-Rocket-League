# Reinforcement Learning for Rocket League

This is a project by Hayden Warren and Joshua Dao

## Requirements

- All required packages in requirements.txt
- Python version 3.9
- Rocket League (Both Steam and Epic are supported)
- RLBot
- Bakkesmod

## Installation

Install the packages via conda:

```
conda create --name <env> --file requirements.txt
```

Once the packages are installed, you need to use the RLArenaCollisionDumper to collect the arena collision geometry and place this in the root.

The RLArenaCollisionDumper can be found at: https://github.com/ZealanL/RLArenaCollisionDumper

You can now run any example<#>.py file to begin training your agent. Training times vary on hardware. In our case, we used a 1070ti and Ryzen 7 3700x with 32GB of RAM.



The following rlbotv<#> folders contain the necesary files to run the bot in Rocket League. The rlbotv<#> folder should be placed in RLbot bots directory and then can be run

To enable visualization during training, please uncomment lines 166 and 167 in the example7.py file. This will allow you to see the bot in action during training.

## Overview

The example.py files are the main training files that include the logging, environment, and runner code.

The data folder contains the checkpoints for the PPO policy created by the training files.

The rlbotv<#> folders contain the necessary files to run the bot in Rocket League. The rlbotv<#> folder should be placed in RLbot bots directory and then can be run.
