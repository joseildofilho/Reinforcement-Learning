class Rules:
    @staticmethod
    def test_victory(board):
        '''
            Tests if the states it's a vitory
            and returns the label of who wins
            PS.: there's  better way of implement, put evering into a single
            loop, but i prefer this way because it's more ditatic
        '''
        for line in board:
            if Rules.check_line(line):
                return line[0]

        for column in range(0, len(board)):
            column_ = []

            for line in board:
                column_.append(line[column])

            if Rules.check_line(column_):
                return column_[0]

        left_diagonal  = []
        right_diagonal = []
        for line in board:
            left_diagonal.append(line[len(left_diagonal)])
            right_diagonal.append(line[len(line) - len(left_diagonal) - 1])

        if Rules.check_line(left_diagonal):
            return left_diagonal[0]
        if Rules.check_line(right_diagonal):
            return right_diagonal[0]

        return False

    @staticmethod
    def test_draw(board):
        if not Rules.test_victory(board):
            for line in board:
                if '' in line:
                    return False
            return True
        return False

    def check_line(line):
        first = line[0]

        for item in range(1,len(line)):
            if item != first:
                return False

        return True


