import pygame

from algorithms import Algorithm
from graph import Graph, Vertex
from typing import List, Optional, Tuple


class Visualization:
    BACKGROUND_COLOR = (255, 255, 255)
    SOURCE_COLOR = (0, 255, 0)
    TARGET_COLOR = (255, 0, 0)
    VERTEX_COLOR = (150, 200, 255)
    WALL_COLOR = (255, 255, 255)

    VERTEX_ACTIVE_COLOR = (0, 255, 0)
    VERTEX_CHECKED_COLOR = (0, 0, 255)
    VERTEX_PATH_COLOR = (255, 0, 0)

    def __init__(self, window_size: Tuple[int, int], board_size: Tuple[int, int]):
        self.board_size = board_size

        pygame.init()
        self.window = pygame.display.set_mode(window_size)
        pygame.display.set_caption('Pathfinder Visualization')

    def visualize(self, algorithm: Algorithm, graph: Graph, source: Vertex, target: Vertex) -> Tuple[List[Vertex], float]:
        clock = pygame.time.Clock()
        self.__draw_board(graph, source, target)
        previous_vertex = None
        generator = algorithm.solve(graph, source, target)

        try:
            while True:
                clock.tick(60)
                vertex = next(generator)
                self.__draw_active_vertex(vertex, previous_vertex)
                previous_vertex = vertex
        except StopIteration as e:
            path, cost = e.value
            self.__draw_path(path)
            pygame.time.wait(1000)

        return path, cost

    def __draw_board(self, graph: Graph, source: Vertex, target: Vertex):
        field_width, field_height = self.__get_field_size()
        self.window.fill(self.BACKGROUND_COLOR)

        for vertex in graph.vertices:
            cost = graph.costs[vertex]

            if vertex == source:
                color = self.SOURCE_COLOR
            elif vertex == target:
                color = self.TARGET_COLOR
            elif cost < 0:
                color = self.WALL_COLOR
            else:
                color = tuple(hue * (1 - cost / 10) for hue in self.VERTEX_COLOR)

            x, y = vertex
            pygame.draw.rect(self.window, color, (x * field_width + 1, y * field_height + 1, field_width - 2, field_height - 2))

        pygame.display.update()

    def __draw_active_vertex(self, vertex: Vertex, previous_vertex: Optional[Vertex]):
        field_width, field_height = self.__get_field_size()

        if previous_vertex:
            x, y = previous_vertex
            pygame.draw.rect(self.window, self.VERTEX_CHECKED_COLOR, (x * field_width + 1, y * field_height + 1, field_width - 2, field_height - 2))

        x, y = vertex
        pygame.draw.rect(self.window, self.VERTEX_ACTIVE_COLOR, (x * field_width + 1, y * field_height + 1, field_width - 2, field_height - 2))

        pygame.display.update()

    def __draw_path(self, path: List[Vertex]):
        field_width, field_height = self.__get_field_size()

        for vertex in path:
            x, y = vertex
            pygame.draw.rect(self.window, self.VERTEX_PATH_COLOR, (x * field_width + 1, y * field_height + 1, field_width - 2, field_height - 2))

        pygame.display.update()

    def __get_field_size(self) -> Tuple[int, int]:
        height = self.window.get_height()
        width = self.window.get_width()
        cols, rows = self.board_size
        return width // cols, height // cols