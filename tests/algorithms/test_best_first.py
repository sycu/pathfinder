from algorithms import BestFirst
from heuristics import Manhattan
from math import sqrt
from .algorithm_test import AlgorithmTest


class TestBestFirst(AlgorithmTest):
    def test_simple_path(self):
        matrix = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]

        path, cost = self.run_algorithm_for_matrix(BestFirst(Manhattan()), matrix, (0, 0), (7, 4))

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

        path, cost = self.run_algorithm_for_matrix(BestFirst(Manhattan()), matrix, (0, 0), (7, 4))

        self.assertEqual(path, [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 4), (6, 4), (7, 4)])
        self.assertEqual(cost, 52 + 4 * sqrt(2))

    def test_impossible_path(self):
        matrix = [
            [1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, -1, 1, 1, 1, 1],
        ]

        path, cost = self.run_algorithm_for_matrix(BestFirst(Manhattan()), matrix, (0, 0), (7, 4))

        self.assertEqual(path, [])
        self.assertEqual(cost, float('inf'))
