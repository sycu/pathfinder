from graph import Graph, Vertex
from heuristics import AbstractHeuristic
from typing import Dict, Generator, List, Optional, Tuple
from .algorithm import Algorithm


class AStar(Algorithm):
    def __init__(self, heuristic: AbstractHeuristic):
        self.heuristic = heuristic

    def solve(self, graph: Graph, source: Vertex, target: Vertex) -> Generator[Vertex, None, Tuple[List[Vertex], float]]:
        open_set = {source}
        f_score = {}
        distances = {}
        sources = {}

        for vertex in graph.vertices:
            distances[vertex] = float('inf')
            f_score[vertex] = float('inf')
            sources[vertex] = None

        f_score[source] = 0.0
        distances[source] = 0.0

        while open_set:
            vertex = min(open_set, key=f_score.get)
            open_set.remove(vertex)

            yield vertex

            if vertex == target:
                return self.__build_path(sources, source, target), distances[target]

            for edge_target, edge_cost in graph.edges[vertex].items():
                tentative_g_score = distances[vertex] + edge_cost
                if tentative_g_score < distances[edge_target]:
                    sources[edge_target] = vertex
                    distances[edge_target] = tentative_g_score
                    f_score[edge_target] = distances[edge_target] + self.heuristic.calculate(edge_target, target)
                    if edge_target not in open_set:
                        open_set.add(edge_target)

        return self.__build_path(sources, source, target), distances[target]

    def __build_path(self, sources: Dict[Vertex, Optional[Vertex]], source: Vertex, target: Vertex) -> List[Vertex]:
        path = []
        while target:
            path = [target] + path
            target = sources[target]

        if path[0] != source:
            return []

        return path
