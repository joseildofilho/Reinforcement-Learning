from grid_world import GridWorld

grid_world = GridWorld.default_game()

states = grid_world.all_states()

V = {state: 0 for state in states}

gamma = 1

Theta = 0.001

delta = 1

while delta > Theta:

    delta = 0
    for state in states:
        v = V[state]
        
        if not grid_world.is_terminal(state):

            v_p = 0 # Accumulator for iterate the sum
            p_a = 1 / len(grid_world._actions[state]) # the probabilites given 
                                                # the function p(s', r | s, a)

            for action in grid_world._actions[state]:
                grid_world.set_state(state)
                reward = grid_world.move(action)
                v_p += p_a * (reward + gamma * V[grid_world.current_state()])

            V[state] = v_p
            aux = abs(v - V[state])
            delta = max(delta, aux)


def show_V(V):
    line = '-' * 10
    print(line)
    for i in range(3):
        for j in range(4):
            val = V.get((i,j),0)
            print('%.1f' % val,' ',end='')
        print()
    print(line)

show_V(V)
