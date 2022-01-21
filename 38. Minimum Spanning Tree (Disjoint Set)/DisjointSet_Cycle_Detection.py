from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(list)

    def add_edge(self, u, v):
        self.edges[u].append(v)


class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {v: v for v in self.vertices}
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1


def is_cycle(graph):

    subsets = DisjointSet(graph.vertices)

    for u in graph.edges:
        uroot = subsets.find(u)

        for v in graph.edges[u]:
            vroot = subsets.find(v)

            if uroot == vroot:
                return True
            else:
                subsets.union(uroot, vroot)


# Driver Code
vertices = [0, 1, 2]
g = Graph(vertices)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 2)

if is_cycle(g):
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")

