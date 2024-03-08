# using Raf's code as a starting point

from player import Player


class BoardError(Exception):
    """Base class for all board errors
    """


class InvalidPositionError(BoardError):
    """Called when a position requested is out of bounds
    """


class PositionOccupiedError(BoardError):
    """Called when a position requested is already occupied
    """


class Board:
    """
    A class representing the board setup and layout
    """

    def __init__(self, size=3) -> None:
        self.size = size
        self.grid = self._create_2d_grid()

    def _create_2d_grid(self) -> list:
        # Build the grid from list of lists, using the size of the board from the initialisation.
        # Use fullstops as the symbol for an 'empty' position on the board.
        grid = []

        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(None)
            grid.append(row)
        return grid

    def is_full(self) -> bool:
        for row in self.grid:
            if None in row:
                return False
        return True

    def is_position_occupied(self, row, col) -> bool:
        return self.grid[row][col] is not None

    def make_move(self, row, col, player) -> None:
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            raise InvalidPositionError("Invalid position")
        if self.is_position_occupied(row, col):
            raise PositionOccupiedError("Position already occupied")

        self.grid[row][col] = player

    def get_winner(self) -> None | Player:
        return self._has_horizontal_winner() or self._has_vertical_winner() or self._has_diagonal_winner()

    def _has_horizontal_winner(self) -> None | Player:
        for row in self.grid:
            horizontal_count = 0
            first_value = row[0]

            # If the first element is an empty space, skip this row
            if first_value is None:
                continue

            # Loop through each element in the row
            for value in row:
                if value == first_value:
                    horizontal_count += 1

            # If the count of same elements is equal to the size of the row, return the player (first element)
            if horizontal_count == self.size:
                return first_value

        # If no winner is found after checking all rows, return None
        return None

    def _has_vertical_winner(self) -> None | Player:
        for column in range(self.size):
            vertical_count = 0
            first_value = self.grid[0][column]

            if first_value is None:
                continue

            for row in range(self.size):
                if self.grid[row][column] == first_value:
                    vertical_count += 1

            if vertical_count == self.size:
                return first_value
        return None

    def _has_diagonal_winner(self) -> None | Player:
        # Check the diagonal from top-left to bottom-right
        top_left_bottom_right_count = 0
        first_value_top_left_bottom_right = self.grid[0][0]

        if first_value_top_left_bottom_right is not None:
            for i in range(self.size):
                if self.grid[i][i] == first_value_top_left_bottom_right:
                    top_left_bottom_right_count += 1

            if top_left_bottom_right_count == self.size:
                return first_value_top_left_bottom_right

        # Check the diagonal from top-right to bottom-left
        top_right_bottom_left_count = 0
        first_value_top_right_bottom_left = self.grid[0][self.size - 1]

        if first_value_top_right_bottom_left is not None:
            for i in range(self.size):
                if self.grid[i][self.size - i - 1] == first_value_top_right_bottom_left:
                    top_right_bottom_left_count += 1

            if top_right_bottom_left_count == self.size:
                return first_value_top_right_bottom_left

        return None

    def __str__(self) -> str:
        # Method for displaying the board with column and row separators, purely for visual purposes

        # set the row dividers of the board
        horizontal_line = "-" * (4 * self.size - 1)

        rows = []
        for row in self.grid:
            formatted_row = []
            for position in row:
                if position is not None:
                    formatted_position = str(position)
                else:
                    formatted_position = " "
                formatted_row.append(formatted_position)
            formatted_row[0] = " " + formatted_row[0]
            # set the column dividers of the board within the row
            rows.append(" | ".join(formatted_row))

        return ("\n" + horizontal_line + "\n").join(rows)
