from graph import Graph, Vertex
from typing import Generator, List, Tuple
from .algorithm import Algorithm


class BestFirstSearch(Algorithm):
    def solve(self, graph: Graph, source: Vertex, target: Vertex) -> Generator[Vertex, None, Tuple[List[Vertex], float]]:
        queue = {source}
        scores = {}
        distances = {}
        sources = {}
        visited = set({})

        for vertex in graph.vertices:
            distances[vertex] = float('inf')
            scores[vertex] = float('inf')
            sources[vertex] = None

        distances[source] = 0.0
        scores[source] = 0.0

        while queue:
            vertex = min(queue, key=scores.get)
            queue.remove(vertex)
            visited.add(vertex)

            yield vertex

            if vertex == target:
                return self._build_path(sources, source, target), distances[target]

            for edge_target, edge_cost in graph.edges[vertex].items():
                if not edge_target in visited:
                    queue.add(edge_target)
                    scores[edge_target] = edge_cost
                    distances[edge_target] = distances[vertex] + edge_cost
                    sources[edge_target] = vertex

        return self._build_path(sources, source, target), distances[target]
