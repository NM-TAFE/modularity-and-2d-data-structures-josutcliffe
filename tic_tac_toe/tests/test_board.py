# Unit testing of the board/position state

import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_has_horizontal_winner(self):
        # Test to check that _has_horizontal_winner can identify a horizontal win position

        # Manually set the values in the grid to create a horizontal winner
        self.board.grid[1][0] = "X"
        self.board.grid[1][1] = "X"
        self.board.grid[1][2] = "X"

        # Use assert to check that the horizontal winner is detected
        winner = self.board._has_horizontal_winner()
        self.assertIsNotNone(winner)
        self.assertEqual(winner, "X")


# Run the tests
if __name__ == '__main__':
    unittest.main()
