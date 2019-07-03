from grid_world import GridWorld
from numpy import Infinity
import random
from utils import *

def update_V(state, value, V):
    V[state][1] += 1
    V[state][0] += (1/V[state][1]) * (value - V[state][0])

grid_world = GridWorld.default_game()

states = grid_world.all_states()

#creates the initial Value function
#state: value v, number of visits.
V = {
        state: [0, 0] if not grid_world.is_terminal(state) else 0
            for state in states
            }

#creates the inital policy
policy = { # a policy, makes easy to know if works
        (0,0): "R",
        (0,1): "R",
        (0,2): "R",
        (1,0): "U",
        (1,2): "R",
        (2,0): "R",
        (2,1): "R",
        (2,2): "R",
        (2,3): "U",
        }

#creates a list of returns for each state
#PS: we use _actions because all the states have an action, except terminal states
returns = {state: 0 for state in grid_world._actions}

gamma = 0.9

Theta = 0.001


'''
    The main loops of this process, it's stoped later
'''
for _ in range(1000):
    grid_world.restart()
    episode = generate_episode(grid_world, policy)
    occurences = set()
    G = 0
    for state, action, reward in zip(episode[-3::-3], episode[-2::-3], episode[-1::-3]):
        G = gamma * G + reward
        if state not in occurences:
            occurences.add(state)
            returns[state] = G
            update_V(state, returns[state], V)

show_V(V)
show_policy(policy)
