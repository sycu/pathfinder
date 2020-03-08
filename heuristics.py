from graph import Vertex
from math import sqrt
from random import randint


class AbstractHeuristic:
    def calculate(self, vertex: Vertex, target: Vertex) -> float:
        raise NotImplemented


class Euclidean(AbstractHeuristic):
    def calculate(self, vertex: Vertex, target: Vertex) -> float:
        return sqrt(abs(vertex[0] - target[0]) ** 2 + abs(vertex[1] - target[1]) ** 2)


class Manhattan(AbstractHeuristic):
    def calculate(self, vertex: Vertex, target: Vertex) -> float:
        return abs(vertex[0] - target[0]) + abs(vertex[1] - target[1])


class Random(AbstractHeuristic):
    def __init__(self, limit: int):
        self.limit = limit

    def calculate(self, vertex: Vertex, target: Vertex) -> float:
        return randint(0, self.limit)
