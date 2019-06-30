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

grid_world = GridWorld.default_game()

states = grid_world.all_states()

#All possible actions
ALL_ACTIONS = ['U', 'D', 'L', 'R']

#creates the initial Value function
#state: value v, number of visits.
V = {
        state: [0, 0] if not grid_world.is_terminal(state) else 0
            for state in states
            }

#creates the inital policy
policy = {action: random.choice(ALL_ACTIONS) for action in grid_world._actions}

#creates a list of returns for each state
#PS: we use _actions because all the states have an action, except terminal states
returns = {state: [] for state in grid_world._actions}

gamma = 0.1

Theta = 0.001


'''
    The main loops of this process, it's stoped later
'''
for _ in range(1000):
    episode = generate_episode(grid_world, policy)
    occurences = set()

    for state, action, reward in zip(episode[-3::-3], episode[-2::-3], episode[-1::-3]):
        if state not in occurences:
            occurences.add(state)
            returns[state].append(reward)
            update_V(state, reward, V)

show_V(V)
show_policy(policy)
