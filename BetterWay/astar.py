from BetterWay.best_first_graph_search import best_first_graph_search
from BetterWay.cost import compute_distance, compute_cost
from ways import graph


def astar(source, target):
    g = graph.load_map_from_csv()
    return best_first_graph_search(graph=g, start=g.get(source), target=g.get(target), compute_cost=compute_cost,
                                   compute_distance=compute_distance)
