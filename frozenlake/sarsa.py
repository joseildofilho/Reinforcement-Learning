import gym
import numpy as np

env = gym.make('FrozenLake8x8-v0')

alpha = 0.9
gamma = 1

get_action = lambda state: np.argmax(Q[state])

e = 0.9
e_greedy_action = lambda state: np.argmax(Q[state]) if np.random.rand() < e else np.random.randint(0,env.nA)


Q = {state: np.random.rand(env.nA)for state in range(env.nS)}

neps = 20000

for t in range(neps):

    S = env.reset()

    A = e_greedy_action(S)

    terminal = False

    while not terminal:

        S_, R, terminal, _ = env.step(A)
        
        A_ = e_greedy_action(S_)

        if terminal:
            Q[S][A] = Q[S][A] + alpha * (R - Q[S][A])
        else:
            Q[S][A] = Q[S][A] + alpha * (R + gamma * Q[S_][A_] - Q[S][A])

        if R != 0 and e > 0.1:
            e *= 0.999
        if alpha > 0.01:
            alpha *= 0.999

        S = S_; A = A_

env.render()
def convert(x):
    return {0:'L', 1:'D',2:'R',3:'U'}[x]

for i in range(env.nS):
    if i % env.nrow == 0:
        print()
    print(convert(get_action(i)), end='')
print()

avg_r = 0
games = 1000

for i in range(games):
    s = env.reset()
    terminal = False

    while not terminal:
        a = np.argmax(Q[s])
        s, r, terminal, _ = env.step(a)
    avg_r += r

avg_r /= games
print(avg_r)
