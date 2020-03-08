from algorithms import AStar, Dijkstra
from creators.matrix_creator import MatrixCreator
from graph import MatrixBuilder
from heuristics import Euclidean, Manhattan, Random, Zero
from visualization import Visualization


if __name__ == '__main__':
    # matrix = [
    #     [1, 2, 3, 4, 5, 6, 1, 2, 3],
    #     [3, 2, 1, 3, 1, 1, 9, 3, 1],
    #     [3, 2, -1, -1, 7, 8, 2, 1, 1],
    #     [3, 2, -1, 1, 1, 3, 1, 1, 1],
    #     [3, 2, -1, 1, 1, 3, 4, 1, 1],
    #     [3, 2, -1, -1, -1, -1, -1, -1, 1],
    #     [3, 2, -1, 1, 1, 1, 1, 1, 1],
    #     [3, 2, -1, 1, -1, -1, -1, -1, -1],
    #     [3, 2, -1, 1, 1, 5, 5, 1, 1],
    #     [3, 2, -1, 1, 1, 1, 1, 4, 1],
    # ]

    creator = MatrixCreator((800, 600), (25, 10))
    matrix, start, end = creator.run()

    euclidean_heuristic = Euclidean()
    manhattan_heuristic = Manhattan()
    random_heuristic = Random(25)
    zero_heuristic = Zero()

    a_star = AStar(zero_heuristic)
    dijkstra = Dijkstra()

    builder = MatrixBuilder()

    visualization = Visualization((800, 600), (25, 10))
    visualization.visualize(a_star, builder.build(matrix), start, end)
