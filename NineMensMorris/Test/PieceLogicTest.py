import unittest
from NineMensMorris.Prod.GameLogic.PieceLogic import OccupiedLocations

class TestOccupiedLocations(unittest.TestCase):

    def setUp(self):
        self.game = OccupiedLocations()

    def test_place_piece_valid(self):
        self.assertTrue(self.game.place_piece(0))
        self.assertEqual(self.game.board[0], 1)

    def test_place_piece_invalid(self):
        self.game.board[1] = 1
        self.assertFalse(self.game.place_piece(1))
        self.assertEqual(self.game.board[1], 1)

    def test_fly_piece_valid(self):
        self.game.board[0] = 1
        self.game.piece_count[1] = 3
        self.assertTrue(self.game.fly_piece(0, 1))
        self.assertEqual(self.game.board[0], 0)
        self.assertEqual(self.game.board[1], 1)

    def test_fly_piece_invalid(self):
        self.game.board[0] = 1
        self.game.piece_count[1] = 4
        self.assertFalse(self.game.fly_piece(0, 1))
        self.assertEqual(self.game.board[0], 1)
        self.assertEqual(self.game.board[1], 0)

    def test_switch_player(self):
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 2)
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 1)

    def test_is_mill_true(self):
        self.game.board[0] = 1
        self.game.board[1] = 1
        self.game.board[2] = 1
        self.assertTrue(self.game.is_mill(1))

    def test_is_mill_false(self):
        self.game.board[0] = 1
        self.game.board[1] = 2
        self.game.board[2] = 1
        self.assertFalse(self.game.is_mill(1))

    def test_remove_opponent_piece_valid(self):
        self.game.board[3] = 2
        self.game.current_player = 1
        self.assertTrue(self.game.remove_opponent_piece(3))
        self.assertEqual(self.game.board[3], 0)

    def test_remove_opponent_piece_invalid(self):
        self.game.board[3] = 1
        self.game.current_player = 1
        self.assertFalse(self.game.remove_opponent_piece(3))
        self.assertEqual(self.game.board[3], 1)

if __name__ == '__main__':
    unittest.main()
