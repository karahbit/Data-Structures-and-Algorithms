#   Created by Elshad Karimov
#   Copyright © 2021 AppMillers. All rights reserved.

from collections import defaultdict


class Graph:
    def __init__(self, numberofVertices):
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topogologicalSortUtil(self, v, visited, stack):
        visited.add(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topogologicalSortUtil(i, visited, stack)

        # stack.insert(0, v)
        stack.append(v)

    def topologicalSort(self):

        visited = set()
        stack = []

        for k in list(self.graph):
            # for k in range(self.numberofVertices):
            if k not in visited:
                self.topogologicalSortUtil(k, visited, stack)

        # print(stack)
        print(stack[::-1])


customGraph = Graph(8)
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")

# g = Graph(6)
# g.addEdge(5, 2)
# g.addEdge(5, 0)
# g.addEdge(4, 0)
# g.addEdge(4, 1)
# g.addEdge(2, 3)
# g.addEdge(3, 1)

customGraph.topologicalSort()
# g.topologicalSort()
