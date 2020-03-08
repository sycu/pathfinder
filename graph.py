from math import sqrt
from typing import List, Tuple

Matrix = List[List[float]]
Vertex = Tuple[int, int]


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = {}
        self.costs = {}  # @TODO: remove?


class MatrixBuilder:
    def build(self, matrix: Matrix) -> Graph:
        graph = Graph()

        rows = len(matrix)
        cols = len(matrix[0])
        sqrt_2 = sqrt(2)

        for y in range(rows):
            for x in range(cols):
                cost = matrix[y][x]
                if cost > -1:
                    vertex = (x, y)
                    graph.vertices.append(vertex)
                    graph.edges[vertex] = {}
                    graph.costs[vertex] = cost

        for vertex in graph.vertices:
            x, y = vertex
            cost = matrix[y][x]

            directions = [
                (-1, 0, 1),
                (1, 0, 1),
                (0, -1, 1),
                (0, 1, 1),
                (-1, -1, sqrt_2),
                (-1, 1, sqrt_2),
                (1, -1, sqrt_2),
                (1, 1, sqrt_2),
            ]

            for dx, dy, cost_multiplier in directions:
                p, q = x + dx, y + dy

                if 0 <= p < cols and 0 <= q < rows:
                    other_vertex = (p, q)
                    other_cost = matrix[q][p]

                    if other_cost > -1:
                        graph.edges[vertex][other_vertex] = other_cost * cost_multiplier
                        graph.edges[other_vertex][vertex] = cost * cost_multiplier

        return graph
