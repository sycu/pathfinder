from algorithms import AStar, Algorithm
from graph import Graph, Vertex
from heuristics import Zero
from typing import Generator, List, Tuple


class Dijkstra(Algorithm):
    def __init__(self):
        self.a_star = AStar(Zero())

    def solve(self, graph: Graph, source: Vertex, target: Vertex) -> Generator[Vertex, None, Tuple[List[Vertex], float]]:
        return self.a_star.solve(graph, source, target)
