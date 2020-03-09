from algorithms import Algorithm
from graph import Graph, Vertex
from typing import Generator, List, Tuple


class BreadthFirst(Algorithm):
    def solve(self, graph: Graph, source: Vertex, target: Vertex) -> Generator[Vertex, None, Tuple[List[Vertex], float]]:
        open = [source]
        closed = set({})
        distances = {}
        sources = {}

        for vertex in graph.vertices:
            distances[vertex] = float('inf')
            sources[vertex] = None

        distances[source] = 0.0

        while open:
            vertex = open.pop(0)
            closed.add(vertex)

            yield vertex

            if vertex == target:
                return self._build_path(sources, source, target), distances[target]

            for edge_target, edge_cost in graph.edges[vertex].items():
                if edge_target not in closed and edge_target not in open:
                    open.append(edge_target)
                    distances[edge_target] = distances[vertex] + edge_cost
                    sources[edge_target] = vertex

        return self._build_path(sources, source, target), distances[target]