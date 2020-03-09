from graph import Graph, Vertex
from heuristics import AbstractHeuristic
from typing import Dict, Generator, List, Tuple
from .algorithm import Algorithm


class AStar(Algorithm):
    def __init__(self, heuristic: AbstractHeuristic):
        self.heuristic = heuristic

    def solve(self, graph: Graph, source: Vertex, target: Vertex) -> Generator[Vertex, None, Tuple[List[Vertex], float]]:
        queue = {source}
        scores = {}
        distances = {}
        sources = {}

        for vertex in graph.vertices:
            distances[vertex] = float('inf')
            scores[vertex] = float('inf')
            sources[vertex] = None

        distances[source] = 0.0
        scores[source] = self._calculate_score(distances, source, target)

        while queue:
            vertex = min(queue, key=scores.get)
            queue.remove(vertex)

            yield vertex

            if vertex == target:
                return self._build_path(sources, source, target), distances[target]

            for edge_target, edge_cost in graph.edges[vertex].items():
                tentative_g_score = distances[vertex] + edge_cost
                if tentative_g_score < distances[edge_target]:
                    sources[edge_target] = vertex
                    distances[edge_target] = tentative_g_score
                    scores[edge_target] = self._calculate_score(distances, edge_target, target)
                    if edge_target not in queue:
                        queue.add(edge_target)

        return self._build_path(sources, source, target), distances[target]

    def _calculate_score(self, distances: Dict[Vertex, float], vertex: Vertex, target: Vertex) -> float:
        return distances[vertex] + self.heuristic.calculate(vertex, target)
