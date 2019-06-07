from rules import Rules

class Environnement:
    '''
        Class that describes the environnement, and 
        holds the environnement.
    '''

    def __init__(self):
        self._board = [["" for _ in range(3)] for _ in range(3)]

    def action(self, x, y, agent):
        self._board[x][y] = agent

    def current_state(self):
        return self._board

    def is_over(self):
        result = Rules.test_victory(self._board)
        if result:
            return result
        result = Rules.test_draw(self._board)
        if result:
            return result
        return False
    def show(self):
        print("-" * 5)
        for line in self._board:
            l = ""
            for item in line:
                if item == '':
                    l += " |"
                else: 
                    l += item + "|"
            l = l[:-1]
            print(l)
            print("-" * 5)
