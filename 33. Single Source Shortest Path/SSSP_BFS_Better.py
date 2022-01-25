from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.edges = defaultdict(list)
        self.v = vertices

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)


def bfs(graph, start, end):
    queue = deque([start])
    visited = set([start])
    pred = [None] * graph.v

    while queue:
        u = queue.popleft()
        for adjacent in graph.edges[u]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
                pred[adjacent] = u
                if adjacent == end:
                    return True, pred

    return False, pred


def print_solution(graph, start, end):
    connected, pred = bfs(graph, start, end)

    if connected:
        crawl = end
        path = [crawl]
        while pred[crawl] is not None:
            path.append(pred[crawl])
            crawl = pred[crawl]

        print(path[::-1])
    else:
        print("Given source and destination are not connected")


# Driver program to test above functions
if __name__ == "__main__":

    graph = Graph(8)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(3, 4)
    graph.add_edge(3, 7)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(4, 7)
    graph.add_edge(5, 6)
    graph.add_edge(6, 7)

    print_solution(graph, 2, 7)

