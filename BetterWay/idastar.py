import math

from BetterWay.cost import compute_cost
from ways import graph, compute_distance


def expand(graph, junction):
    children = []
    for link in junction[3]:
        children.append(graph.get(link[1]))
    return children


def getPath(child_to_parent, start, current):
    path = []
    while start != current:
        path.append(current)
        current = child_to_parent[current]
    path.append(current)
    path.reverse()
    return path


def idastar(source, target):
    g = graph.load_map_from_csv()
    return ida_star(g, g.get(source), g.get(target))


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
