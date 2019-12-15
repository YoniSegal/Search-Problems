import csv

from BetterWay import graph
from BetterWay.best_first_graph_search import best_first_graph_search
from BetterWay.cost import compute_cost


def fake(source, target):
    return 0


def ucs(source, target):
    g = graph.load_map_from_csv()
    f = open("UCSRuns.txt", "w+")

    with open('problems.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile, delimiter=',', quotechar="'"))
    for problem in data:
        source = int(problem[0])
        target = int(problem[1])
        time, path = best_first_graph_search(graph=g, start=g.get(source), target=g.get(target),
                                             compute_cost=compute_cost, compute_distance=fake)
        print(' '.join(str(j[0]) + " " for j in path))
        f.write(str(time))
    f.close()
    return path
