class Graph:
    def __init__(self, vertices, edges, nodes):
        self.V = vertices
        self.edges = edges
        self.nodes = nodes
        self.MST = [None] * self.V

    def print_solution(self):
        for i in range(1, self.V):
            s = self.nodes[self.MST[i]]
            d = self.nodes[i]
            w = self.edges[i][self.MST[i]]
            print("%s - %s: %s" % (s, d, w))

    def min_weight(self, weight, visited):
        smallest = float("inf")
        for v in range(self.V):
            if not visited[v] and weight[v] < smallest:
                smallest = weight[v]
                smallest_index = v
        return smallest_index

    def prims(self):
        weight = [float("inf")] * self.V
        weight[0] = 0
        self.MST[0] = -1
        visited = [False] * self.V

        for _ in range(self.V):
            u = self.min_weight(weight, visited)
            for v in range(self.V):
                if not visited[v] and self.edges[u][v]:
                    if weight[v] > self.edges[u][v]:
                        weight[v] = self.edges[u][v]
                        self.MST[v] = u
            visited[u] = True

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
