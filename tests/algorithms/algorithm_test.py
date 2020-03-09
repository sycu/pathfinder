from algorithms import Algorithm
from graph import List, Matrix, MatrixBuilder, Tuple, Vertex
from unittest import TestCase


class AlgorithmTest(TestCase):
    def run_algorithm_for_matrix(self, algorithm: Algorithm, matrix: Matrix, source: Vertex, target: Vertex) -> Tuple[List[Vertex], float]:
        builder = MatrixBuilder()
        generator = algorithm.solve(builder.build(matrix), source, target)

        try:
            while True:
                next(generator)
        except StopIteration as e:
            path, cost = e.value

        return path, cost
