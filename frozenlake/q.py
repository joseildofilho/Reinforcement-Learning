import gym
import numpy as np

env = gym.make('FrozenLake8x8-v0')

Q = {}
for s in range(env.nS):
    Q[s] = np.random.rand(4)

alpha  = 0.33
epslon = gamma = 1

episodes = 10000

e_greedy = lambda s: np.argmax(Q[s]) if epslon > np.random.rand() else np.random.randint(0,env.nA)

for episode in range(episodes):


    S = env.reset()

    terminal = False

    while not terminal:

        A = e_greedy(S)

        S_, R, terminal, _ = env.step(A)

        if terminal:
            Q[S][A] = Q[S][A] + alpha * (R - Q[S][A])
        else:
            Q[S][A] = Q[S][A] + alpha * (R + gamma * np.max(Q[S_]) - Q[S][A])

        if epslon > 0.01 and R != 0:
            epslon *= 0.9999

        if alpha > 0.01:
            alpha *= 0.99999

        S = S_

actions_map = {0:'L', 1:'D', 2:'R', 3:'U'}

env.render()

for q in Q:
    if q % env.nrow == 0:
        print()
    print(actions_map[np.argmax(Q[q])],end='')
print()

avg_r = 0
for i in range(100):
    s = env.reset()
    terminal = False

    while not terminal:
        a = np.argmax(Q[s])
        s, r, terminal, _ = env.step(a)
    avg_r += r

avg_r /= 100
print(avg_r)
