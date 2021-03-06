import pygame

from graph import Matrix, Vertex
from typing import Optional, Tuple
from visualization import Visualization


class MatrixCreator:
    BACKGROUND_COLOR = Visualization.BACKGROUND_COLOR
    SOURCE_COLOR = Visualization.SOURCE_COLOR
    TARGET_COLOR = Visualization.TARGET_COLOR
    VERTEX_COLOR = Visualization.VERTEX_COLOR
    WALL_COLOR = Visualization.WALL_COLOR

    def __init__(self, window_size: Tuple[int, int], board_size: Tuple[int, int]):
        self.board_size = board_size

        pygame.init()
        self.window = pygame.display.set_mode(window_size)
        pygame.display.set_caption('Pathfinder Creator')

    def run(self, matrix: Optional[Matrix], source: Vertex, target: Vertex) -> Tuple[Matrix, Vertex, Vertex]:
        clock = pygame.time.Clock()

        if not matrix:
            matrix = [[1 for x in range(self.board_size[0])] for y in range(self.board_size[1])]

        place_source = True

        self.__redraw(matrix, source, target)

        run = True
        while run:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    button = event.button
                    x, y = pygame.mouse.get_pos()
                    col = x // (self.window.get_width() // self.board_size[0])
                    row = y // (self.window.get_height() // self.board_size[1])

                    if button == 1 or button == 3:
                        diff = 2 if button == 1 else -2
                        matrix[row][col] += diff

                        if matrix[row][col] < -1:
                            matrix[row][col] = -1
                        elif matrix[row][col] > 10:
                            matrix[row][col] = 10
                    elif button == 2:
                        if place_source:
                            source = (col, row)
                        else:
                            target = (col, row)
                        place_source = not place_source

                    self.__redraw(matrix, source, target)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return matrix, source, target

    def __redraw(self, matrix: Matrix, source: Tuple[int, int], target: Tuple[int, int]):
        self.window.fill(self.BACKGROUND_COLOR)
        height = self.window.get_height()
        width = self.window.get_width()

        cols, rows = self.board_size

        field_width = width // cols
        field_height = height // rows

        for y in range(rows):
            for x in range(cols):
                cost = matrix[y][x]

                if (x, y) == source:
                    color = self.SOURCE_COLOR
                elif (x, y) == target:
                    color = self.TARGET_COLOR
                elif cost < 0:
                    color = self.WALL_COLOR
                else:
                    color = tuple(hue * (1 - cost / 10) for hue in self.VERTEX_COLOR)

                pygame.draw.rect(self.window, color, (x * field_width + 1, y * field_height + 1, field_width - 2, field_height - 2))

        pygame.display.update()
