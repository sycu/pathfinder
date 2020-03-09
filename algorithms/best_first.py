from algorithms import AStar
from graph import Vertex
from typing import Dict


class BestFirst(AStar):
    def _calculate_score(self, distances: Dict[Vertex, float], vertex: Vertex, target: Vertex) -> float:
        return self.heuristic.calculate(vertex, target)
