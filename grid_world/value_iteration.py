from grid_world import GridWorld
import random
from numpy import Infinity

grid_world = GridWorld.default_game()

states = grid_world.all_states()

V = {state: 0 for state in states}

ALL_ACTIONS = ['U', 'D', 'L', 'R']

policy = {action: random.choice(ALL_ACTIONS) for action in grid_world._actions}

gamma = 1

Theta = 0.001

delta = 1

while delta > Theta:

    delta = 0
    for state in states:
        v = V[state]
        
        if not grid_world.is_terminal(state):

            p_a = 1 / len(grid_world._actions[state]) # the probabilites given 
                                                # the function p(s', r | s, a)
            
            for action in grid_world._actions[state]:
                grid_world.set_state(state)
                reward = grid_world.move(action)
                test = p_a * (reward + gamma * V[grid_world.current_state()])
                if V[state] < test:
                    V[state] = test

            aux = abs(v - V[state])
            delta = max(delta, aux)

for state in states:
    if not grid_world.is_terminal(state):
        max_act_val = -Infinity
        max_act     = ''
        for action in grid_world._actions[state]:
            grid_world.set_state(state)
            reward = grid_world.move(action)
            test = p_a * (reward + gamma * V[grid_world.current_state()])
            if test > max_act_val:
                max_act_val = test
                max_act     = action
        policy[state] = max_act

def show_V(V):
    line = '-' * 10
    print(line)
    for i in range(3):
        for j in range(4):
            val = V.get((i,j),0)
            print('%.1f' % val,' ',end='')
        print()
    print(line)

def show_policy(V):
    line = '-' * 10
    print(line)
    for i in range(3):
        for j in range(4):
            val = V.get((i,j)," ")
            print(val,' ',end='')
        print()
    print(line)


show_V(V)
show_policy(policy)
