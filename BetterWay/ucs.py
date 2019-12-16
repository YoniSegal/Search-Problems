import csv
import datetime
import time
from timeit import timeit

from BetterWay import graph
from BetterWay.best_first_graph_search import best_first_graph_search
from BetterWay.cost import compute_cost


def fake(lon1, lat1, lon2, lat2):
    return 0


def ucs(source, target):
    g = graph.load_map_from_csv()
    f = open(r"C:\Users\yonis\Desktop\ComputerScience\AI\ex1\MyWay\results\UCSRuns.txt", "w+")

    times = []
    with open('problems.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile, delimiter=',', quotechar="'"))
    for problem in data:
        source = int(problem[0])
        target = int(problem[1])
        start = datetime.datetime.now().replace(second=0)
        time, path = best_first_graph_search(graph=g, start=g.get(source), target=g.get(target),
                                             compute_cost=compute_cost, compute_distance=fake)
        end = datetime.datetime.now().replace(second=0)
        times.append((end - start).total_seconds())
        print(' '.join(str(j[0]) + " " for j in path))
        f.write(str(time) + "\n")
    f.close()
    average = sum(times) / len(times)
    print("Average UCS: " + str(average))
    # time, path = best_first_graph_search(graph=g, start=g.get(source), target=g.get(target),
    #                                      compute_cost=compute_cost, compute_distance=fake)
    return path
