from grid_world import GridWorld
from numpy import Infinity
import random

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


grid_world = GridWorld.painful_game()

states = grid_world.all_states()

#All possible actions
ALL_ACTIONS = ['U', 'D', 'L', 'R']

#creates the initial Value function
V = {
        state: random.random() if not grid_world.is_terminal(state) else 0
            for state in states
            }

#creates the inital policy
policy = {action: random.choice(ALL_ACTIONS) for action in grid_world._actions}

gamma = 0.9

Theta = 0.001

windy = 0.9 # the probability of movement, for any side

'''
    The main loops of this process, it's stoped later
'''
while True:
    #policy evaluation
    delta = 1
    while delta > Theta: 
        delta = 0
        for state in states:
            v = V[state] 
            if state in policy:

                action = policy[state]

                grid_world.set_state(state)
                reward = grid_world.move(action)
                V[state] = windy * (reward + gamma * V[grid_world.current_state()])
                delta = max(delta, abs(v - V[state]))

    #policy improvement
    policy_stable = True

    for state in states:
        if state in policy:

            old_action = policy[state]
    
            value_action = -Infinity
            action_p = ''

            for action in grid_world._actions[state]:
                grid_world.set_state(state)
                reward = grid_world.move(action)
                test = windy * (reward + gamma * V[grid_world.current_state()])
                if value_action < test:
                    value_action = test
                    action_p = action
            policy[state] = action_p
            if old_action != policy[state]:
                policy_stable = False 

    if policy_stable:
        break
    show_policy(policy)

show_V(V)
show_policy(policy)
