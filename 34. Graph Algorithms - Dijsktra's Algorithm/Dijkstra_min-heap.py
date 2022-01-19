from collections import defaultdict
import heapq


def dijkstra(edges, start):
    graph = defaultdict(list)
    for src, dest, w in edges:
        graph[src].append((dest, w))

    min_heap = [(0, start)]
    visited = {}
    path = defaultdict(list)
    while min_heap:
        d, node = heapq.heappop(min_heap)
        if node not in visited:
            visited[node] = d
            for edge, w in graph[node]:
                if edge not in visited:
                    heapq.heappush(min_heap, (d + w, edge))
                    if path[edge] == []:
                        path[edge].append(node)

    return visited, path


print(dijkstra([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 2))


edges = [
    ["A", "B", 2],
    ["A", "C", 5],
    ["B", "C", 6],
    ["B", "D", 1],
    ["B", "E", 3],
    ["C", "F", 8],
    ["D", "E", 4],
    ["E", "G", 9],
    ["F", "G", 7],
]
print(dijkstra(edges, "A"))
