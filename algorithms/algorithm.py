from graph import Graph, Vertex
from typing import Generator, List, Tuple


class Algorithm:
    def solve(self, graph: Graph, source: Vertex, target: Vertex) -> Generator[Vertex, None, Tuple[List[Vertex], float]]:
        raise NotImplemented()
