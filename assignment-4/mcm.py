from ReinforcementLearning.GridWorld import GridWorld
import json
import numpy as np
from copy import deepcopy

env_vars = {
    "rewards":{(0, 3): '1', (1, 3): '-1'},
    "walls":{(1,1): '*'},
    "dimension":(3,4),
    "initial_state":(0,0)
}

enviroment = GridWorld(**env_vars)
policy = enviroment.getRandomPolicy()
enviroment.printBoard()
print('\nPolicy')
enviroment.printPolicy(policy)
print(enviroment.qtable)