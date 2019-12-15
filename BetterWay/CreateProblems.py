from BetterWay.Graph import Graph
from ways import load_map_from_csv
import csv
import random


def creatGraph():
    roads = load_map_from_csv(r"C:\Users\yonis\Desktop\ComputerScience\AI\ex1\MyWay\db\israel.csv")
    G = Graph(len(roads))
    for link in roads.iterlinks():
        G.addEdge(link.source, link.target)
    return G


def creatProblems():
    G = creatGraph()
    writer = csv.writer(open("problems.csv", 'w', newline=''))
    i = 0
    while i < 100:
        v = random.randint(0, G.V)
        u = random.randint(0, G.V)
        if G.isReachable(u, v, 1000):
            print(i)
            i += 1
            row = [u, v]
            writer.writerow(row)


if __name__ == '__main__':
    from sys import argv

    creatProblems()
