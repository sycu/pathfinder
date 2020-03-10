import pickle
import sys

from algorithms import AStar, BestFirst, BiAStar, BreadthFirst, Dijkstra
from creators.matrix_creator import MatrixCreator
from graph import Matrix, MatrixBuilder, Vertex
from heuristics import Euclidean, Manhattan, Zero
from typing import Optional, Tuple
from visualization import Visualization


def load_matrix(path: str) -> Optional[Tuple[Tuple[int, int], Matrix, Vertex, Vertex]]:
    with open(path, 'rb') as file:
        return pickle.load(file)


def save_matrix(path: str, board_size: Tuple[int, int], matrix: Matrix, source: Vertex, target: Vertex) -> None:
    with open(path, 'wb') as file:
        pickle.dump((board_size, matrix, source, target), file, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage:')
        print('python pathfinder.py [matrix_file] [cols] [rows]')
        exit(1)

    matrix_file = sys.argv[1]
    board_size = (int(sys.argv[2]), int(sys.argv[3]))

    try:
        board_size, matrix, source, target = load_matrix(matrix_file)
    except FileNotFoundError:
        matrix = None
        source = (0, 0)
        target = (board_size[0] - 1, board_size[1] - 1)

    creator = MatrixCreator((800, 600), board_size)
    matrix, source, target = creator.run(matrix, source, target)

    euclidean_heuristic = Euclidean()
    manhattan_heuristic = Manhattan()
    zero_heuristic = Zero()

    a_star = AStar(manhattan_heuristic)
    best_first = BestFirst(manhattan_heuristic)
    bi_a_star = BiAStar(zero_heuristic)
    breadth_first = BreadthFirst()
    dijkstra = Dijkstra()

    builder = MatrixBuilder()
    graph = builder.build(matrix)

    algorithms = {
        'A*': a_star,
        'Best First Search': best_first,
        'Bidirectional A*': bi_a_star,
        'Breadth First Search': breadth_first,
        'Dijkstra': dijkstra
    }

    visualization = Visualization((800, 600), board_size)

    save_matrix(matrix_file, board_size, matrix, source, target)

    for name, algorithm in algorithms.items():
        path, cost = visualization.visualize(algorithm, graph, source, target)
        print('%s: %f, path: %s' % (name, cost, path))
