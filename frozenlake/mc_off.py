import gym
import numpy as np

env = gym.make('FrozenLake-v0')

Q      = {}
C      = {}
policy = {}
for s in range(env.nS):
    Q[s]   = [np.random.rand() for _ in range(env.nA)]
    C[s]   = [0] * env.nA
    policy[s] = np.argmax(Q[s])

def create_episode():
    episode = []
    S = env.reset()
    A = np.random.choice(np.arange(env.nA), p=b[s])
    R = 0

    terminal = False
    while not terminal:
        S_, R, terminal, _ = env.step(A)
        episode.append((S, A, R))
        A = np.random.choice(np.arange(env.nA), p=b[s])
        S = S_

    return episode

def create_b():
    b = {}
    for s in range(env.nS):
        aux = np.sum(Q[s])
        if aux == 0:
            b[s] = np.zeros(env.nA) + 0.25
        else:
            b[s] = np.divide(Q[s], aux)
            b[s] = np.array([0.01 if not i else i for i in b[s]])
    return b

nIter = 10000

gamma = 1
i = 0

for e in range(nIter):

    b       = create_b()
    episode = create_episode()

    G = 0
    W = 1

    for S, A, R in reversed(episode):
        G       = gamma * G + R 
        C[S][A] = C[S][A] + W
        Q[S][A] = Q[S][A] +  (W / C[S][A]) * (G - Q[S][A])

        policy[S] = np.argmax(Q[S])

        if A != policy[S]:
            i += 1
            break
        W = W / b[S][A]

actions = {0:'L', 1:'D', 2:'R', 3:'U'}

env.render()
for i in range(env.nS):
    if i % env.nrow == 0:
        print()
    print(actions[policy[i]],'', end='')
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
