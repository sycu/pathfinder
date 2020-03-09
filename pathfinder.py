from algorithms import AStar, BestFirst, BreadthFirst, Dijkstra
from creators.matrix_creator import MatrixCreator
from graph import MatrixBuilder
from heuristics import Euclidean, Manhattan, Zero
from visualization import Visualization

if __name__ == '__main__':
    creator = MatrixCreator((800, 600), (25, 10))
    matrix, start, end = creator.run()

    euclidean_heuristic = Euclidean()
    manhattan_heuristic = Manhattan()
    zero_heuristic = Zero()

    a_star = AStar(manhattan_heuristic)
    best_first = BestFirst(manhattan_heuristic)
    breadth_first = BreadthFirst()
    dijkstra = Dijkstra()

    builder = MatrixBuilder()

    visualization = Visualization((800, 600), (25, 10))
    visualization.visualize(a_star, builder.build(matrix), start, end)
