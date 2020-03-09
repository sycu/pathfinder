from algorithms import BreadthFirst
from math import sqrt
from .algorithm_test import AlgorithmTest


class TestBreadthFirst(AlgorithmTest):
    def test_simple_path(self):
        matrix = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]

        path, cost = self.run_algorithm_for_matrix(BreadthFirst(), matrix, (0, 0), (7, 4))

        self.assertEqual(path, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 1), (5, 2), (6, 3), (7, 4)])
        self.assertEqual(cost, 3 + 4 * sqrt(2))

    def test_weighted_path(self):
        matrix = [
            [1, 1, 1, 1, 1, 1,  1, 1],
            [1, 1, 1, 1, 1, 1, -1, 1],
            [1, 1, 1, 1, 1, 1, -1, 1],
            [1, 1, 1, 1, 1, 1, -1, 1],
            [1, 1, 1, 1, 1, 1, 50, 1],
        ]

        path, cost = self.run_algorithm_for_matrix(BreadthFirst(), matrix, (0, 0), (7, 4))

        self.assertEqual(path, [(0, 0), (1, 0), (2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 4)])
        self.assertEqual(cost, 3 + 53 * sqrt(2))

    def test_impossible_path(self):
        matrix = [
            [1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, -1, 1, 1, 1, 1],
        ]

        path, cost = self.run_algorithm_for_matrix(BreadthFirst(), matrix, (0, 0), (7, 4))

        self.assertEqual(path, [])
        self.assertEqual(cost, float('inf'))
