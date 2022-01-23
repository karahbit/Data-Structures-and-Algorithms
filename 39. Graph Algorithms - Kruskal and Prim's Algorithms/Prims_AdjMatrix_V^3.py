#   Created by Elshad Karimov
#   Copyright © 2021 AppMillers. All rights reserved.

# Prims Algorithm  in Python


class Graph:
    def __init__(self, vertices, edges, nodes):
        self.V = vertices
        self.edges = edges
        self.nodes = nodes
        self.MST = []

    def print_solution(self):
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))

    def prims(self):
        visited = [0] * self.V
        e = 0
        visited[0] = True
        while e < self.V - 1:
            smallest = float("inf")
            for i in range(self.V):
                if visited[i]:
                    for j in range(self.V):
                        if not visited[j] and self.edges[i][j]:
                            if smallest > self.edges[i][j]:
                                smallest = self.edges[i][j]
                                s, d = i, j
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            e += 1
        self.print_solution()


edges = [
    [0, 5, 13, 0, 15],
    [5, 0, 10, 8, 0],
    [13, 10, 0, 6, 20],
    [0, 8, 6, 0, 0],
    [15, 0, 20, 0, 0],
]
nodes = ["A", "B", "C", "D", "E"]
g = Graph(5, edges, nodes)
g.prims()
