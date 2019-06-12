from rules import Rules
from state import State

class Environnement:
    '''
        Class that describes the environnement, and 
        holds the environnement.
    '''

    def __init__(self):
        self._board = State()

    def action(self, x, y, agent):
        self._board.current[x][y] = agent

    def current_state(self):
        s = State()
        s.current = self._board._copy_current()
        return s
    def is_over(self):
        result = Rules.test_victory(self._board.current)
        if result:
            return result
        result = Rules.test_draw(self._board.current)
        if result:
            return result
        return False

    def show(self):
        print("-" * 5)
        for line in self._board.current:
            l = ""
            for item in line:
                if item == '':
                    l += " |"
                else: 
                    l += item + "|"
            l = l[:-1]
            print(l)
            print("-" * 5)
