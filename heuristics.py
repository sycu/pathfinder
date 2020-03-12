from graph import Vertex


class AbstractHeuristic:
    def calculate(self, vertex: Vertex, target: Vertex) -> float:
        raise NotImplemented


class Euclidean(AbstractHeuristic):
    def calculate(self, vertex: Vertex, target: Vertex) -> float:
        return abs(vertex[0] - target[0]) ** 2 + abs(vertex[1] - target[1]) ** 2


class Manhattan(AbstractHeuristic):
    def calculate(self, vertex: Vertex, target: Vertex) -> float:
        return abs(vertex[0] - target[0]) + abs(vertex[1] - target[1])


class Zero(AbstractHeuristic):
    def calculate(self, vertex: Vertex, target: Vertex) -> float:
        return 0
