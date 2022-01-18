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
                    path[edge].append(node)

    return visited, path


print(dijkstra([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 2))

