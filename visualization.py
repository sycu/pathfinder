import pygame

from algorithms import Algorithm
from graph import Graph, Vertex
from typing import List, Optional, Tuple


class Visualization:
    BACKGROUND_COLOR = (255, 255, 255)
    VERTEX_ACTIVE_COLOR = (0, 255, 0)
    VERTEX_CHECKED_COLOR = (0, 0, 255)
    VERTEX_NOT_CHECKED_COLOR = (100, 100, 100)
    VERTEX_PATH_COLOR = (255, 0, 0)

    def __init__(self, window_size: Tuple[int, int], board_size: Tuple[int, int]):
        self.board_size = board_size

        pygame.init()
        self.window = pygame.display.set_mode(window_size)
        pygame.display.set_caption('Pathfinder')

    def visualize(self, algorithm: Algorithm, graph: Graph, source: Vertex, target: Vertex) -> Tuple[List[Vertex], float]:
        clock = pygame.time.Clock()
        generator = algorithm.solve(graph, source, target)
        checked_vertices = []

        try:
            while True:
                clock.tick(30)
                vertex = next(generator)
                self.__redraw(graph, checked_vertices, [], vertex)
                checked_vertices.append(vertex)
        except StopIteration as e:
            path, cost = e.value
            self.__redraw(graph, checked_vertices, path, None)
            pygame.time.wait(1000)

        return path, cost

    def __redraw(self, graph: Graph, checked_vertices: List[Vertex], path: List[Vertex], active_vertex: Optional[Vertex]):
        self.window.fill(self.BACKGROUND_COLOR)
        height = self.window.get_height()
        width = self.window.get_width()

        cols, rows = self.board_size

        field_width = width // cols
        field_height = height // rows

        for vertex in graph.vertices:
            cost_color = 25 * graph.costs[vertex]

            if vertex == active_vertex:
                color = self.VERTEX_ACTIVE_COLOR
            elif vertex in path:
                color = self.VERTEX_PATH_COLOR
            elif vertex in checked_vertices:
                color = self.VERTEX_CHECKED_COLOR
            else:
                color = (cost_color, 255 - cost_color, 0)

            x, y = vertex
            pygame.draw.rect(self.window, color, (x * field_width + 1, y * field_height + 1, field_width - 2, field_height - 2))

        pygame.display.update()
