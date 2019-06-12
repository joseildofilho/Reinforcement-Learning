import unittest
from main import Agent, play_game
from environnement import Environnement
from rules import Rules

class AgentTest(Agent):
    def __init__(self, actions, mark):
        Agent.__init__(self,mark)
        self._actions = actions
        self._i = 0

    def take_action(self, environnement):
        action = self._actions[self._i]
        self._i += 1
        environnement.action(action[0], action[1], self._mark)

class TestGame(unittest.TestCase):
    def test_win_line(self):
        self.winner = [
                (0,0),
                (0,1),
                (0,2)
                ]
        self.loser = [
                (1,0),
                (1,1),
                (1,2)
                ]
        a_1 = AgentTest(self.winner, 'O')
        a_2 = AgentTest(self.loser, 'X')

        environnement = Environnement()

        test = play_game(a_1, a_2, environnement)

        self.assertEqual(test, 'O')

    def test_win_column(self):
        self.winner = [
                (0,0),
                (1,0),
                (2,0)
                ]
        self.loser = [
                (0,1),
                (0,2),
                (1,2)
                ]
        a_1 = AgentTest(self.winner, 'O')
        a_2 = AgentTest(self.loser, 'X')

        environnement = Environnement()

        test = play_game(a_1, a_2, environnement)

        self.assertEqual(test, 'O')

    def test_win_diagonal(self):
        self.winner = [
                (0,0),
                (1,1),
                (2,2)
                ]
        self.loser = [
                (0,1),
                (0,2),
                (1,2)
                ]
        a_1 = AgentTest(self.winner, 'O')
        a_2 = AgentTest(self.loser, 'X')

        environnement = Environnement()

        test = play_game(a_1, a_2, environnement)

        self.assertEqual(test, 'O')

    def test_check_line_false(self):
        x = ["o", "o", ""]
        self.assertFalse(Rules.check_line(x))
        x = ["", "o", ""]
        self.assertFalse(Rules.check_line(x))
        x = ["", "", ""]
        self.assertFalse(Rules.check_line(x))
        x = ["o", "o", "x"]
        self.assertFalse(Rules.check_line(x))

    def test_check_line_true(self):
        x = ["o", "o", "o"]
        self.assertTrue(Rules.check_line(x))

