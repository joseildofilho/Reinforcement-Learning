class GridWorld:
    def __init__(self, height, width, start = (0,0), actions=[], rewards=[]):
        '''
            Define the envoriment of the game Grid World.
            @params:
                height  : define the height of the grid.
                width   : define the width of the grid.
                start   : a tuple where the game will begin.
                actions : a map where each state has a set of possible moves
                rewards : a map where each state has a set of rewards
        '''
        self._height = height
        self._width  = width

        self.set_state(start)

        self._actions = actions
        self._rewards = rewards

    def set_state(self, start):
        '''
            Sets the state where the player will be 
        '''
        self._i = start[0]
        self._j = start[1]

    def current_state(self):
        '''
            the current state of the game
        '''
        return (self._i, self._j)

    def is_terminal(self, state):
        '''
            Tests if given state is it terminal.
            P.S.: the terminals states have no available actions
        '''
        return state not in self._actions

    def move(self, action):
        '''
            Make's amove and return the reward of the new state
        '''
        if action in self._actions[(self._i, self._j)]:
            if   action == 'U':
                self._i += 1

            elif action == 'D':
                self._i -= 1

            elif action == 'L':
                self._j += 1

            elif action == 'R':
                self._j -= 1

        return self._rewards.get((self._i, self._j), 0)
    
    @staticmethod
    def default_game():
        '''
            Creates a game
        '''

        actions = {
                (0,0): ['R', 'D'],
                (0,1): ['R', 'L'],
                (0,2): ['R', 'L', 'D'],
                (1,0): ['U', 'D'],
                (1,2): ['R', 'D', 'U'],
                (2,0): ['R', 'U'],
                (2,1): ['R', 'L'],
                (2,2): ['R', 'L', 'U'],
                (2,3): ['L', 'U']
                }
        rewards = {
                (0,3): 1,
                (1,3): -1
                }

        return GridWorld(3, 4, (0, 2), actions, rewards)

if __name__ == '__main__':
    grid = GridWorld.default_game()

