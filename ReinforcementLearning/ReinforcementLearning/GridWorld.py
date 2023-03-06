import numpy as np
from copy import deepcopy

class GridWorld:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)
        self.board = np.full(self.dimension, ' ')
        self.actions = self.getActions()
        self.qtable = {}
        self.explored = 0
        self.exploited = 0
        self.generateBoard()
        self.initialQtable()
    
    def generateBoard(self):
        for key, value in self.rewards.items():
            self.board[key] = value
        
        for key, value in self.walls.items():
            self.board[key] = value

    def printBoard(self):
        for x in self.board:
            print('\n' + '------' * self.dimension[0])
            for index, y in enumerate(x):
                print(f'| {y} ', end='')
                if index == self.dimension[0]:
                    print('|', end='')
        print('\n' + '------'  * self.dimension[0])
    
    def getCurrentState(self):
        return self.current_state

    def getPossibleActions(self, state):
        possible_actions = []
        x, y = state
        if x > 0 and self.board[x-1][y] != '*':
            possible_actions.append('U')
        if x < self.dimension[0]-1 and self.board[x+1][y] != '*':
            possible_actions.append('D')
        if y > 0 and self.board[x][y-1] != '*':
            possible_actions.append('L')
        if y < self.dimension[1]-1 and self.board[x][y+1] != '*':
            possible_actions.append('R')
        return possible_actions

    def getActions(self):
        actions = {}
        for index, value in np.ndenumerate(self.board):
            actions[index] = self.getPossibleActions(index)
        return actions
    
    def initialQtable(self):
        self.qtable = {}
        for state in self.actions:
            self.qtable[state]={}
            for move in self.actions[state]:
                self.qtable[state][move]=0

    def getRandomPolicy(self):
        policy = {}
        for state in self.actions:
            policy[state] = np.random.choice(self.actions[state])
        return policy

    def printPolicy(self, policy):
        line = ""
        counter = 0
        print('------'  * self.dimension[0])
        for item in policy:
            line += f"| {policy[item]} "
            counter += 1
            if counter > self.dimension[0]:
                print(line, end = '|\n')
                print('------' * self.dimension[0])
                counter = 0
                line = ""
        print(line)
