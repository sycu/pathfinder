from graph import Graph, Vertex
from typing import Dict, Generator, List, Optional, Tuple
from .algorithm import Algorithm


class Dijkstra(Algorithm):
    def solve(self, graph: Graph, source: Vertex, target: Vertex) -> Generator[Vertex, None, Tuple[List[Vertex], float]]:
        distances = {}
        sources = {}
        vertices = set({})

        for vertex in graph.vertices:
            distances[vertex] = float('inf')
            sources[vertex] = None
            vertices.add(vertex)

        distances[source] = 0.0

        while vertices:
            vertex = min(vertices, key=distances.get)
            vertices.remove(vertex)

            yield vertex

            if vertex == target:
                return self.__build_path(sources, source, target), distances[target]

            for edge_target, edge_cost in graph.edges[vertex].items():
                if edge_target in vertices:
                    distance = distances[vertex] + edge_cost
                    if distance < distances[edge_target]:
                        distances[edge_target] = distance
                        sources[edge_target] = vertex

        return [], distances[target]

    def __build_path(self, sources: Dict[Vertex, Optional[Vertex]], source: Vertex, target: Vertex) -> List[Vertex]:
        path = []
        while target:
            path = [target] + path
            target = sources[target]

        if path[0] != source:
            return []

        return path
