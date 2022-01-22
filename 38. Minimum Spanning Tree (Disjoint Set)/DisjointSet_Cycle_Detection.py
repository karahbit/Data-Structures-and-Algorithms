from collections import defaultdict
import DisjointSet as ds


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(list)

    def add_edge(self, u, v):
        self.edges[u].append(v)


def is_cycle(graph):

    subsets = ds.DisjointSet(graph.vertices)

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

