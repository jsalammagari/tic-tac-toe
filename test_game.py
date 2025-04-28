import unittest
from game import Game, Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_state(self):
        self.assertEqual(self.game.board, [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
        self.assertIsNone(self.game.current_player)
        self.assertIsNone(self.game.winner)
        self.assertFalse(self.game.draw)

    def test_switch_players(self):
        player1 = Player('X')
        player2 = Player('O')
        self.game.current_player = player1
        self.game.switch_players()
        self.assertEqual(self.game.current_player, player2)
        self.game.switch_players()
        self.assertEqual(self.game.current_player, player1)

    def test_make_move(self):
        self.game.current_player = Player('X')
        self.game.current_player.move = (1, 1)
        self.game.make_move()
        self.assertEqual(self.game.board, [[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']])

    def test_check_win_row(self):
        self.game.board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.game.current_player = Player('X')
        self.assertTrue(self.game.check_win())

    def test_check_win_column(self):
        self.game.board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        self.game.current_player = Player('X')
        self.assertTrue(self.game.check_win())

    def test_check_win_diagonal(self):
        self.game.board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.game.current_player = Player('X')
        self.assertTrue(self.game.check_win())

    def test_check_draw(self):
        self.game.board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
        self.assertTrue(self.game.check_draw())

if __name__ == '__main__':
    unittest.main()
