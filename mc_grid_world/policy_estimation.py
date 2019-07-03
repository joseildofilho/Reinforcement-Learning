from grid_world import GridWorld
from numpy import Infinity
from utils import *

import random

grid_world = GridWorld.default_game()

states = grid_world.all_states()

#All possible actions
ALL_ACTIONS = ['U', 'D', 'L', 'R']

#creates the initial Q function
#state: value q, number of visits.
Q = {}
for state in states:
    if not grid_world.is_terminal(state):
        for action in grid_world._actions[state]:
            Q.update({(state, action) : [0,0]})

#creates the inital e-policy
policy = {}
for state in grid_world._actions:
    actions = grid_world._actions[state]
    p = 1 / len(actions)
    actions = {action: p for action in actions}
    policy.update({state:actions})

gamma = 0.9
epslon = 0.1

'''
    The main loops of this process, it's stoped later
'''
for _ in range(100000):
    grid_world.restart()
    episode = generate_episode_from_e_policy(grid_world, policy)
    G = 0
    for state, action, reward in zip(episode[-3::-3], episode[-2::-3], episode[-1::-3]):

        G = gamma * G + reward
        Q[(state, action)][1] += 1
        Q[(state, action)][0] += (1 / Q[(state, action)][1]) * (G - Q[(state, action)][0])

        # argmax_a Q(S_t, a)
        max_q = -Infinity
        action_max = ''
        actions = grid_world._actions[state]
        for a in actions:
            test = Q.get((state, a), [-Infinity])[0]
            if test > max_q:
                max_q = test
                action_max = a

        ratio = (epslon / len(actions))
        for action in actions:
            if action == action_max:
                policy[state][action] = 1 - epslon + ratio
            else:
                policy[state][action] = ratio
show_policy(policy)
