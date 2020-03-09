from algorithms import AStar
from graph import Graph, Vertex
from typing import Dict, Generator, List, Optional, Tuple


class BiAStar(AStar):
    def solve(self, graph: Graph, source: Vertex, target: Vertex) -> Generator[Vertex, None, Tuple[List[Vertex], float]]:
        front_queue = {source}
        back_queue = {target}
        front_scores = {}
        back_scores = {}
        front_distances = {}
        back_distances = {}
        front_sources = {}
        back_sources = {}

        front_closed = set({})
        back_closed = set({})

        for vertex in graph.vertices:
            front_distances[vertex] = float('inf')
            back_distances[vertex] = float('inf')
            front_scores[vertex] = float('inf')
            back_scores[vertex] = float('inf')
            front_sources[vertex] = None
            back_sources[vertex] = None

        front_distances[source] = 0.0
        front_scores[source] = self._calculate_score(front_distances, source, target)

        back_distances[target] = 0.0
        back_scores[target] = self._calculate_score(back_distances, target, source)

        while front_queue and back_queue:
            front_vertex = min(front_queue, key=front_scores.get)
            front_queue.remove(front_vertex)
            front_closed.add(front_vertex)

            yield front_vertex

            if front_vertex in back_closed:
                return self._build_bi_path(front_sources, back_sources, source, front_vertex, target), front_distances[front_vertex] + back_distances[front_vertex]

            self._visit_neighbors(front_vertex, target, graph, front_distances, front_sources, front_scores, front_queue)

            back_vertex = min(back_queue, key=back_scores.get)
            back_queue.remove(back_vertex)
            back_closed.add(back_vertex)

            yield back_vertex

            if back_vertex in front_closed:
                return self._build_bi_path(front_sources, back_sources, source, back_vertex, target), front_distances[back_vertex] + back_distances[back_vertex]

            self._visit_neighbors(back_vertex, source, graph, back_distances, back_sources, back_scores, back_queue)

        return self._build_path(front_sources, source, target), front_distances[target]


    def _build_bi_path(self, front_sources: Dict[Vertex, Optional[Vertex]], back_sources: Dict[Vertex, Optional[Vertex]], source: Vertex, middle: Vertex, target: Vertex) -> List[Vertex]:
        front_path = self._build_path(front_sources, source, middle)
        back_path = self._build_path(back_sources, target, middle)

        return list(dict.fromkeys(front_path + list(reversed(back_path))))
