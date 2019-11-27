from queue import PriorityQueue

from ways import graph


def best_first_graph_search(source, target, compute_distance):
    # frontier = PriorityQueue(compute_distance)  # Priority Queue
    # frontier.put(source)
    # closed_list = set()
    # while frontier:
    #     node = frontier.get()
    #     if node == target:
    #         return node
    #     closed_list.add(node.state)
    #     for child in node.expand(problem):
    #         if child.state not in closed_list and child not in frontier:
    #             frontier.append(child)
    #         elif child in frontier and compute_distance(child) < frontier[child]:
    #             del frontier[child]
    #             frontier.append(child)
    return None


def ucs(source, target, compute_distance):
    g = graph.load_map_from_csv()
    return best_first_graph_search(source, target, compute_distance)
