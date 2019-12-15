# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:04:18 2019

@author: vered
"""

# program to check if there is exist a path between two vertices
# of a graph

from collections import defaultdict


# This class represents a directed graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def actions(self, u):
        return self.graph[u];

    # Use BFS to check path between s and d
    def isReachable(self, s, d, limit):
        # Mark all the vertices as not visited
        visited = [False] * (self.V)
        level = 0
        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            if level == limit:
                return False
            # Dequeue a vertex from queue
            n = queue.pop(0)
            # If this adjacent node is the destination node,
            # then return true
            if n == d:
                return True
            #  Else, continue to do BFS
            level += 1
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        # If BFS is complete without visited d
        return False
