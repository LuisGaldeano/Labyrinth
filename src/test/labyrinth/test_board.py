from src.labyrinth.models.board import Board
from src.main import labyrinth
from unittest import TestCase


class BoardTest(TestCase):
    def setUp(self):
        self.board = Board()

    def test_walls(self):
        walls_position, _ = self.board.walls(base_labyrinth=labyrinth)
        expected_walls = [[1, 0], [1, 4], [2, 4], [3, 1], [3, 7], [4, 1], [4, 7]]
        self.assertEqual(walls_position, expected_walls)

    def test_actual_position(self):
        base_labyrinth = [[1, 1, 1, '.', '.', '.', '.', '.', '.'],
                          ['#', '.', '.', '.', '#', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
                          ['.', '#', '.', '.', '.', '.', '.', '#', '.'],
                          ['.', '#', '.', '.', '.', '.', '.', '#', '.']]

        expected_position = [[0, 0], [0, 1], [0, 2]]
        actual_position = self.board.actual_position(base_labyrinth)
        self.assertEqual(actual_position, expected_position)
