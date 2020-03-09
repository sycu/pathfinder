import pygame

from graph import Matrix
from typing import Tuple


class MatrixCreator:
    BACKGROUND_COLOR = (255, 255, 255)

    def __init__(self, window_size: Tuple[int, int], board_size: Tuple[int, int]):
        self.board_size = board_size

        pygame.init()
        self.window = pygame.display.set_mode(window_size)
        pygame.display.set_caption('Pathfinder Creator')

    def run(self) -> Tuple[Matrix, Tuple[int, int], Tuple[int, int]]:
        clock = pygame.time.Clock()
        matrix = [[1 for x in range(self.board_size[0])] for y in range(self.board_size[1])]

        place_start = True
        start = (0, 0)
        end = (self.board_size[0] - 1, self.board_size[1] - 1)

        self.__redraw(matrix, start, end)

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
                        if place_start:
                            start = (col, row)
                        else:
                            end = (col, row)
                        place_start = not place_start

                    self.__redraw(matrix, start, end)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return matrix, start, end


    def __redraw(self, matrix: Matrix, start: Tuple[int, int], end: Tuple[int, int]):
        self.window.fill(self.BACKGROUND_COLOR)
        height = self.window.get_height()
        width = self.window.get_width()

        cols, rows = self.board_size

        field_width = width // cols
        field_height = height // rows

        for y in range(rows):
            for x in range(cols):
                cost = matrix[y][x]
                cost_color = 255 - 25 * cost if cost > -1 else 0
                color = (cost_color, cost_color, cost_color)

                if (x, y) == start:
                    color = (0, 255, 0)
                elif (x, y) == end:
                    color = (255, 0, 0)

                pygame.draw.rect(self.window, color, (x * field_width + 1, y * field_height + 1, field_width - 2, field_height - 2))

        pygame.display.update()
