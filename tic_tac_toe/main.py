from random import random
from rules import Rules
from environnement import Environnement
from state import State

def play_game(agent_1, agent_2, environnement, show=False):

    current_player = agent_1

    test = environnement.is_over()

    while not test:
 
        current_player.take_action(environnement)

        if show:
            environnement.show()

        if current_player == agent_1:
            current_player = agent_2
        else:
            current_player = agent_1

        current_state = environnement.current_state()

        agent_1.update_history(current_state)
        agent_2.update_history(current_state)

        test = environnement.is_over()
    if show:    
        print("Updating Value function ...")

    agent_1.update_value_fun(environnement)
    agent_2.update_value_fun(environnement)

    return test

class Agent:

    def __init__(self, mark, enemy_mark=None):
        self._history = []
        self._mark = mark
        self._enemy_mark = enemy_mark if enemy_mark else mark + '@'
        self._has_tree = False
        self.alpha = 0.5
    
    def create_game_tree(self):
        self._tree = State()
        self._has_tree = True
        self._game_tree_rec(self._tree)

    def _game_tree_rec(self, state):
        victory = Rules.test_victory(state.current)
        draw = Rules.test_draw(state.current)
        if not (victory or draw):
            state.s_p =  state.fill_empty(self._mark)
            state.s_p += state.fill_empty(self._enemy_mark)
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

    def update_history(self, state):
        if self._has_tree:
            if len(self._history) == 0:
                self._history.append(self._tree)
            last = self._history[-1]
            # theres a bug
            i = last.s_p.index(state)
            self._history.append(last.s_p[i])
 
    def update_value_fun(self, environnement):
        value = self._history[-1].v
        for state in self._history[::-1]:
            state.v -= self.alpha * value
            value = state.v

    def new_game(self):
        self._history = []

class AgentAuto(Agent):

    def take_action(self, environnement):
        if len(self._history):
            action = self._history[-1]
        else:
            action = self._tree
            self._history.append(action)

        futures = action.s_p
        next_action = futures[0]
        for state in futures:
            if next_action.v <= state.v:
                next_action = state

        pos = action.diff(next_action)
        environnement.action(pos[0], pos[1], self._mark)
        
class AgentUser(Agent):

    def take_action(self, environnement):
        x = int(input('X: '))
        y = int(input('Y: '))
        environnement.action(x,y, self._mark)        

if __name__ == '__main__':

    agent_1_mark = 'O'
    agent_2_mark = 'X'

    agent_1 = AgentAuto(agent_1_mark, agent_2_mark)
    agent_2 = AgentAuto(agent_2_mark, agent_1_mark)

    agent_1.create_game_tree()
    agent_2.create_game_tree()

    agent_1_win = 0
    agent_2_win = 0
    draw = 0

    for i in range(100000):
        environnement = Environnement()
    
        agent_1.new_game()
        agent_2.new_game()

        if i % 2 == 0:
            win = play_game(agent_2, agent_1, environnement)
        else:
            win = play_game(agent_1, agent_2, environnement)

        if agent_1_mark == win:
            agent_1_win += 1
        elif agent_2_mark == win:
            agent_2_win += 1
        else:
            draw += 1

    print(agent_1_win, agent_2_win, draw)
            
