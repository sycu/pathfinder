from algorithms import AStar
from heuristics import Manhattan
from math import sqrt
from .algorithm_test import AlgorithmTest


class TestAStar(AlgorithmTest):
    def test_simple_path(self):
        matrix = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]

        path, cost = self.run_algorithm_for_matrix(AStar(Manhattan()), matrix, (0, 0), (7, 4))

        self.assertEqual(path, [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 4), (6, 4), (7, 4)])
        self.assertEqual(cost, 3 + 4 * sqrt(2))

    def test_weighted_path(self):
        matrix = [
            [1, 1, 1, 1, 1, 1,  1, 1],
            [1, 1, 1, 1, 1, 1, -1, 1],
            [1, 1, 1, 1, 1, 1, -1, 1],
            [1, 1, 1, 1, 1, 1, -1, 1],
            [1, 1, 1, 1, 1, 1, 50, 1],
        ]

        path, cost = self.run_algorithm_for_matrix(AStar(Manhattan()), matrix, (0, 0), (7, 4))

        self.assertEqual(path, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 1), (7, 2), (7, 3), (7, 4)])
        self.assertEqual(cost, 9 + 1 * sqrt(2))

    def test_impossible_path(self):
        matrix = [
            [1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, -1, 1, 1, 1, 1],
        ]

        path, cost = self.run_algorithm_for_matrix(AStar(Manhattan()), matrix, (0, 0), (7, 4))

        self.assertEqual(path, [])
        self.assertEqual(cost, float('inf'))
