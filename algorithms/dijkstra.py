from algorithms import AStar
from heuristics import Zero


class Dijkstra(AStar):
    def __init__(self):
        super().__init__(Zero())
