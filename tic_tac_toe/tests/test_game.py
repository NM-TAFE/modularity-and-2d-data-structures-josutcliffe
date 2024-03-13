# Unit testing of the game logic

import unittest
from game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_get_winner(self):
        # Test to check if the get_winner method detects the player/winner of the game

        # Manually set the state of the board for a horizontal win for 'X'
        self.game.board.grid = [
            ['X', 'X', 'X'],
            [None, None, None],
            [None, None, None]]

        # Use assert to call get_winner, checking that it matches 'X' as defined in the game state
        self.assertEqual(self.game.get_winner(), 'X')


# Run the tests
if __name__ == '__main__':
    unittest.main()
