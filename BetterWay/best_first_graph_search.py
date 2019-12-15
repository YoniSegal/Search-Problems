from queue import PriorityQueue


def expand(graph, junction):
    children = []
    for link in junction[3]:
        children.append(graph.get(link[1]))
    return children


def notIn(i, visited):
    for node in visited:
        if node == i:
            return False
    return True


def getPath(child_to_parent, start, current, compute_cost):
    total_time = 0
    path = []
    while start != current:
        path.append(current)
        total_time += compute_cost(child_to_parent[current], current)
        current = child_to_parent[current]
    path.append(current)
    path.reverse()
    return total_time, path


def best_first_graph_search(graph, start, target, compute_cost, compute_distance):
    child_to_parent = {}
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))

    while queue:
        cost, junction = queue.get()
        if junction == target:
            return getPath(child_to_parent, start, target, compute_cost)
        if len(junction[3]) == 0:
            continue
        visited.add(junction)
        for i in expand(graph, junction):
            if notIn(i, visited):
                if len(i[3]) != 0:
                    child_to_parent[i] = junction
                total_cost = cost + compute_cost(junction, i) + compute_distance(i, target)
                queue.put((total_cost, i))
    return None
