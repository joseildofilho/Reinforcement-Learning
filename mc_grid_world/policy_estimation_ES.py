from grid_world import GridWorld
from numpy import Infinity
from utils import *

import random

grid_world = GridWorld.painful_game()

states = grid_world.all_states()

#creates the initial Q function
#state: value q, number of visits.
Q = {}
for state in states:
    if not grid_world.is_terminal(state):
        for action in grid_world._actions[state]:
            Q.update({(state, action) : [0,0]})

policy = {}

for state in grid_world._actions:
    action = random.choice(ALL_ACTIONS)
    while action not in grid_world._actions[state]:
        action = random.choice(ALL_ACTIONS)
    policy.update({state:action})

gamma = 0.9

show_policy(policy)

'''
    The main loops of this process, it's stoped later
'''
for _ in range(100000):
    episode = generate_episode_random_start(grid_world, policy)
    occurences = set()
    G = 0
    for state, action, reward in zip(episode[-3::-3], episode[-2::-3], episode[-1::-3]):
        G = gamma * G + reward
        if (state, action) not in occurences:
            occurences.add((state, action))
            Q[(state, action)][1] += 1
            Q[(state, action)][0] += (1 / Q[(state, action)][1]) * (G - Q[(state, action)][0])
            max_q = -Infinity
            action_max = ''
            actions = grid_world._actions[state]
            for a in actions:
                test = Q.get((state, a), [-Infinity])[0]
                if test > max_q:
                    max_q = test
                    action_max = a
            policy[state] = action_max
        else:
            break

show_policy(policy)
