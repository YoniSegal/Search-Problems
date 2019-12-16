import csv
import datetime

import matplotlib.pyplot as plt
from BetterWay.best_first_graph_search import best_first_graph_search
from BetterWay.cost import compute_distance, compute_cost, getLink
from BetterWay import graph
from ways.draw import plot_path


def get_roads(path):
    roads = []
    for i in range(len(path) - 1):
        link = getLink(path[i], path[i + 1])
        roads.append(link)
    return roads


def getIds(path):
    p = []
    for junc in path:
        p.append((junc[0]))
    return p


def astar(source, target):
    g = graph.load_map_from_csv()
    f = open(r"C:\Users\yonis\Desktop\ComputerScience\AI\ex1\MyWay\results\AStarRuns.txt", "w+")
    heuristic = []
    actual = []
    times = []
    i = 0
    with open('problems.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile, delimiter=',', quotechar="'"))
    for problem in data:
        source = int(problem[0])
        target = int(problem[1])
        heuristic.append(compute_distance(g.get(source)[1], g.get(source)[2], g.get(target)[1], g.get(target)[2]))
        start = datetime.datetime.now().replace(second=0)

        time, path = best_first_graph_search(graph=g, start=g.get(source), target=g.get(target),
                                             compute_cost=compute_cost,
                                             compute_distance=compute_distance)
        end = datetime.datetime.now().replace(second=0)
        times.append((end - start).total_seconds())
        print(' '.join(str(j[0]) + " " for j in path))
        actual.append(time)
        f.write(str(time) + "\n")
        if i < 10:
            plot_path(str(i) + ".png", g, getIds(path))
        i += 1
    f.close()
    average = sum(times) / len(times)
    print("Average A*: " + str(average))
    plt.title("AStar")
    plt.plot(heuristic, actual, 'o')
    plt.xlabel("Heuristic time")
    plt.ylabel("Actual time")
    plt.savefig(r"C:\Users\yonis\Desktop\ComputerScience\AI\ex1\MyWay\results\AStar.png")
    plt.show()
    # time, path = best_first_graph_search(graph=g, start=g.get(source), target=g.get(target),
    #                                      compute_cost=compute_cost,
    #                                      compute_distance=compute_distance)
    return path
