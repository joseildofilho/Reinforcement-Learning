from random import random
from rules import Rules
from environnement import Environnement

def play_game(agent_1, agent_2, environnement, show=False):

    current_player = agent_1

    while not environnement.is_over():

        current_player.take_action(environnement)

        current_player = agent_1 if current_player == agent_2 else agent_2

        current_state = environnement.current_state()

        if show:
            environnement.show()

        agent_1.update_history(current_state)
        agent_2.update_history(current_state)

    agent_1.update_value_fun(environnement)
    agent_2.update_value_fun(environnement)

class State:
    def __init__(self, state=None):
        self.current = [['' for _ in range(3)] for _ in range(3)]
        self.s_p = []
        if state:
            self.current = state.current
            self.v = 0.5
            self.s_p = state.s_p

class Agent:

    def __init__(self):
        self._history = []
        self.V = []
    
    def create_game_tree(self):
        self._tree = State()

    def _game_tree_rec(self, state):
        pass

    def take_action(self, environnement):
        pass

    def update_history(self, environnement):
        pass

class AgentUser(Agent):
    def __init__(self, mark):
        self._mark = mark

    def take_action(self, environnement):
        x = int(input('X: '))
        y = int(input('Y: '))
        environnement.action(x,y, self.mark)        

if __name__ == '__main__':
    agent_1 = AgentUser('O')
    agent_2 = AgentUser('X')
    
    environnement = Environnement()

    play_game(agent_1, agent_2, environnement, True)
