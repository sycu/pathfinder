from graph import Graph, Vertex
from typing import Dict, Generator, List, Optional, Tuple


class Algorithm:
    def solve(self, graph: Graph, source: Vertex, target: Vertex) -> Generator[Vertex, None, Tuple[List[Vertex], float]]:
        raise NotImplemented()

    def _build_path(self, sources: Dict[Vertex, Optional[Vertex]], source: Vertex, target: Vertex) -> List[Vertex]:
        path = []
        while target:
            path = [target] + path
            target = sources[target]

        if path[0] != source:
            return []

        return path
