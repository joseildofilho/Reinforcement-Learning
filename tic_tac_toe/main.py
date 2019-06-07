from random import random
from rules import Rules
from environnement import Environnement

def play_game(agent_1, agent_2, environnement, show=False):

    current_player = agent_1

    test = environnement.is_over()

    while not test:
 
        current_player.take_action(environnement)

        if show:
            environnement.show()

        current_player = agent_1 if current_player == agent_2 else agent_2

        current_state = environnement.current_state()

        agent_1.update_history(current_state)
        agent_2.update_history(current_state)

        test = environnement.is_over()

    agent_1.update_value_fun(environnement)
    agent_2.update_value_fun(environnement)

    return test

class State:
    def __init__(self, state=None):
        self.current = [['' for _ in range(3)] for _ in range(3)]
        self.v = 0.5
        self.s_p = []
        if state:
            self.current = state.current
            self.v = 0.5
            self.s_p = state.s_p

class Agent:

    def __init__(self, mark):
        self._history = []
        self.V = []
        self._mark = mark
        self._enemy_mark = mark + '@'
    
    def create_game_tree(self):
        self._tree = State()

    def _game_tree_rec(self, state):
        victory = Rules.test_victory(state.current)
        draw = Rules.test_draw(state.current)
        if not victory or draw:
            state.s_p =  State.fill_empty(self._mark)
            state.s_p += State.fill_empty(self._enemy_mark)
            for state_ in state.s_p:
                self._game_tree_rec(state_)
        elif victory:
            if victory == self._mark:
                state.v = 1
            else:
                state.v = -1
        elif draw:
            state.v = 0

    def take_action(self, environnement):
        pass

    def update_history(self, environnement):
        pass

    def update_value_fun(self, environnement):
        pass

class AgentUser(Agent):

    def take_action(self, environnement):
        x = int(input('X: '))
        y = int(input('Y: '))
        environnement.action(x,y, self._mark)        

if __name__ == '__main__':
    agent_1 = AgentUser('O')
    agent_2 = AgentUser('X')
    
    environnement = Environnement()

    play_game(agent_1, agent_2, environnement, True)
