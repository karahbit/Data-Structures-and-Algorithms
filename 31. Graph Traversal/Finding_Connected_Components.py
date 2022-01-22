#   Created by Elshad Karimov
#   Copyright © 2021 AppMillers. All rights reserved.


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)


def dfs(graph, temp, v, visited):
    visited.append(v)

    temp.append(v)

    for i in graph.gdict[v]:
        if i not in visited:
            temp = dfs(graph, temp, i, visited)
    return temp


def connected_components(graph):
    visited = []
    cc = []

    for i in graph.gdict:
        if i not in visited:
            temp = []
            cc.append(dfs(graph, temp, i, visited))
    return cc


customDict = {
    "a": ["b"],
    "b": ["a"],
    "c": ["d"],
    "d": ["c", "e"],
    "e": ["c", "e"],
    "f": [],
}


g = Graph(customDict)

print(connected_components(g))
