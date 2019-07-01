from grid_world import GridWorld
from numpy import Infinity
import random

def show_V(V):
    line = '-' * 10
    print(line)
    for i in range(3):
        for j in range(4):
            val = V.get((i,j),0)
            try:
                val = val[0]
            except:
                pass
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

def update_V(state, value, V):
    V[state][1] += 1
    V[state][0] += (1/V[state][1]) * (value - V[state][0])


T_max = 100

def generate_episode(grid_world, policy):
    i = 0

    action_start = random.choice(list(grid_world._actions.keys()))

    grid_world.set_state(action_start)

    history = [grid_world.current_state()] # state

    history.append(policy[history[-1]]) # action

    history.append(grid_world.move(history[-1])) # reward

    while (i < T_max) and (not grid_world.is_terminal(grid_world.current_state())):

        history.append(grid_world.current_state())

        history.append(policy[history[-1]])

        history.append(grid_world.move(history[-1])) # reward

        i += 1

    return history

grid_world = GridWorld.painful_game()

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

#creates the inital policy
policy = {action: random.choice(ALL_ACTIONS) for action in grid_world._actions}

policy = {}

for state in grid_world._actions:
    action = random.choice(ALL_ACTIONS)
    while action not in grid_world._actions[state]:
        action = random.choice(ALL_ACTIONS)
    policy.update({state:action})

policy__ = { # a good policy, makes easy to know if works
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

gamma = 0.9

show_policy(policy)

'''
    The main loops of this process, it's stoped later
'''
for _ in range(100000):
    episode = generate_episode(grid_world, policy)
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
