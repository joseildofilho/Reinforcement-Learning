import numpy as np
import random
import matplotlib.pyplot as plt

class Bandit:
    def __init__(self, k = 10):
        self.k = k
        self._arms = []
        self._arms_values = []

        for i in range(self.k):
            arm_value = self._norm_rand(0, 1, 3)

            self._arms.append(arm_value[0])
            self._arms_values.append(arm_value[1])

        self._best_arm = np.argmax(self._arms_values)
        self._best_selected_count = 0
        self._best_history = []

    def _norm_rand(self, mu, sigma, offset):
        offset = (np.random.rand() * 2 * offset) - offset
        def aux():
            return np.random.normal(mu, sigma) + offset
        return (aux, offset)

    def use_arm(self, arm):
        if self._best_arm == arm:
            self._best_selected_count += 1
            self._best_history.append(1)
        else:
            self._best_history.append(0)
        return self._arms[arm]()

class Action:
    def __init__(self, initial_reward=0):
        self._reward = initial_reward
        self._times_used = 0
        self._mean = initial_reward

    def use(self, reward):
        self._reward += reward
        self._times_used += 1
        self._mean = self._reward / self._times_used

    def estimated(self):
        return self._mean

    def show(self):
        print("Estimated Value:", self._mean, "Used:", self._times_used)

class Actions:

    def __init__(self): 
        self._actions = []

    def add(self, action):
        self._actions.append(action)

    def max_action(self):
        index_aux = 0
        max_aux   = self._actions[index_aux]

        for index, action in enumerate(self._actions):
            if max_aux.estimated() < action.estimated():
                max_aux = action
                index_aux = index

        return (max_aux, index_aux)
    def show_information(self):
        for index, action in enumerate(self._actions):
            print("postion:", index)
            action.show()
            print()

    def pick_action(self, e):
        if np.random.rand() < e:
            action_index = random.randint(0, len(self._actions)-1)
            return (self._actions[action_index], action_index)
        else:
            return self.max_action()

def run_problem(k=20, initial_reward=0, steps=2000, e=0):
    bandit = Bandit(k)
        
    actions = Actions()
    
    total_reward = 0
      
    for i in range(k):
        actions.add(Action(initial_reward))
    
    for step in range(steps, 0, -1):
        action_greedy, action_index_greedy = actions.pick_action(e)
    
        reward = bandit.use_arm(action_index_greedy)
        action_greedy.use(reward)

        total_reward += reward
    return bandit._best_history
 
def run_attemps(num_attemps = 1000, e=0):

    historys   = []
    for attempt in range(num_attemps):
        x = run_problem(e=e)
        historys.append(x)
    
    total_history = np.zeros(len(historys[0]))
    for history in historys:
        total_history = total_history + np.array(history)

    total_history = total_history/num_attemps

    return total_history


if __name__ == '__main__':
    
    e_09 = run_attemps(e=0.9)
    e_02 = run_attemps(e=0.2)
    e_01  = run_attemps(e=0.1)
    e_001 = run_attemps(e=0.01)
    e_0   = run_attemps(e=0)

    plt.plot(e_09)
    plt.plot(e_02)
    plt.plot(e_01)
    plt.plot(e_001)
    plt.plot(e_0)
    plt.legend(["e=0.9","e=0.2","e=0.1","e=0.01","e=0"])
    plt.show()
