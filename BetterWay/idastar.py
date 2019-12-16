import csv
import datetime
import math
import matplotlib.pyplot as plt

from BetterWay.cost import compute_cost
from ways import compute_distance
from BetterWay import graph


def expand(graph, junction):
    children = []
    for link in junction[3]:
        children.append(graph.get(link[1]))
    return children


def getPath(child_to_parent, start, current):
    total_time = 0
    path = []
    while start != current:
        path.append(current)
        total_time += compute_cost(child_to_parent[current], current)
        current = child_to_parent[current]
    path.append(current)
    path.reverse()
    return total_time, path


def idastar(source, target):
    g = graph.load_map_from_csv()
    f = open(r"C:\Users\yonis\Desktop\ComputerScience\AI\ex1\MyWay\results\IdaStarRuns.txt", "w+")
    heuristic = []
    actual = []
    i = 0
    times = []
    with open('problems.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile, delimiter=',', quotechar="'"))
    for problem in data:
        if i == 5:
            break
        source = int(problem[0])
        target = int(problem[1])
        heuristic.append(compute_distance(g.get(source)[1], g.get(source)[2], g.get(target)[1], g.get(target)[2]))
        start = datetime.datetime.now().replace(second=0)
        time, path = ida_star(g, g.get(source), g.get(target))
        end = datetime.datetime.now().replace(second=0)
        times.append((end - start).total_seconds())
        print(' '.join(str(j[0]) + " " for j in path))
        actual.append(time)
        f.write(str(time) + "\n")
        i += 1
    f.close()
    average = sum(times) / len(times)
    print("Average IDA*: " + str(average))
    plt.title("IdaStar")
    plt.plot(heuristic, actual, 'o')
    plt.xlabel("Heuristic time")
    plt.ylabel("Actual time")
    plt.savefig(r"C:\Users\yonis\Desktop\ComputerScience\AI\ex1\MyWay\results\IdaStar.png")
    plt.show()
    # time, path = ida_star(g, g.get(source), g.get(target))
    return path


def ida_star(graph, source, target):
    global closed
    global new_limit
    global child_to_parent
    child_to_parent = {}
    closed = set()
    new_limit = compute_distance(source[1], source[2], target[1], target[2])
    while True:
        f_limit = new_limit
        new_limit = math.inf
        sol = search(graph, source, target, 0, f_limit, compute_distance)
        if sol:
            return getPath(child_to_parent, source, target)


def search(graph, source, target, g, f_limit, heuristic):
    global new_limit
    closed.add(source)
    new_f = g + heuristic(source[1], source[2], target[1], target[2])
    if new_f > f_limit:
        new_limit = min(new_limit, new_f)
        return None
    if source == target:
        return [target]
    for child in expand(graph, source):
        if child in closed:
            continue
        child_to_parent[child] = source
        sol = search(graph, child, target, g + compute_cost(source, child), f_limit, heuristic)
        if sol:
            return sol
    return None
