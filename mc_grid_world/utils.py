import random
import numpy as np

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

#All possible actions
ALL_ACTIONS = ['U', 'D', 'L', 'R']

def get_action(actions):
    acts = []
    P    = []
    for action in actions:
        acts.append(action)
        P.append(actions[action])

    return np.random.choice(acts, p=P)
    
T_max = 100

def generate_episode_from_e_policy(grid_world, policy):
    history = []

    history.append(grid_world.current_state())
    history.append(get_action(policy[history[-1]]))
    history.append(grid_world.move(history[-1]))

    while not grid_world.is_terminal(grid_world.current_state()):

        history.append(grid_world.current_state())
        history.append(get_action(policy[history[-1]]))
        history.append(grid_world.move(history[-1]))

    return history


    


def generate_episode_random_start(grid_world, policy):

    action_start = random.choice(list(grid_world._actions.keys()))

    grid_world.set_state(action_start)

    return generate_episode(grid_world, policy)

def generate_episode(grid_world, policy):
    '''
        Only works for deterministic policy
    '''

    history = [] # state

    states_set = set()

    state = grid_world.current_state()

    history.append(state)

    states_set.add(state)

    history.append(policy[history[-1]]) # action
    history.append(grid_world.move(history[-1])) # reward

    while ((not grid_world.is_terminal(grid_world.current_state())) 
        and not grid_world.current_state() in states_set):

        state = grid_world.current_state()

        history.append(state)
        states_set.add(state)

        history.append(policy[history[-1]])

        history.append(grid_world.move(history[-1])) # reward

    return history


