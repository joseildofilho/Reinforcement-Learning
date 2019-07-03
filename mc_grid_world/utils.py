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

#All possible actions
ALL_ACTIONS = ['U', 'D', 'L', 'R']

T_max = 100

def generate_episode_random_start(grid_world, policy):
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

