from algorithms import AStar, BestFirst, BiAStar, BreadthFirst, Dijkstra
from creators.matrix_creator import MatrixCreator
from graph import MatrixBuilder
from heuristics import Euclidean, Manhattan, Zero
from visualization import Visualization

if __name__ == '__main__':
    creator = MatrixCreator((800, 600), (40, 30))
    matrix, start, end = creator.run()

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

    algos = [
        a_star,
        best_first,
        bi_a_star,
        breadth_first,
        dijkstra
    ]

    visualization = Visualization((800, 600), (40, 30))

    for algo in algos:
        visualization.visualize(algo, graph, start, end)
