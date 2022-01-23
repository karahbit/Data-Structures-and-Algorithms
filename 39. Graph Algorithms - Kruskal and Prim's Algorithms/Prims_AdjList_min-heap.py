# Prims Algorithm  in Python
from collections import defaultdict
import heapq


def prims(edges, start):
    graph = defaultdict(list)
    for s, d, w in edges:
        graph[s].append((d, w))

    mst = []
    visited = set([start])

    min_heap = []
    for d, w in graph[start]:
        min_heap.append((w, start, d))
    heapq.heapify(min_heap)

    while min_heap:
        w, s, d = heapq.heappop(min_heap)
        if d not in visited:
            visited.add(d)
            mst.append([s, d, w])
            for to_next, w in graph[d]:
                if to_next not in visited:
                    heapq.heappush(min_heap, (w, d, to_next))

    return mst


def print_solution(mst):
    for s, d, w in mst:
        print("%s - %s: %s" % (s, d, w))


edges = [
    ["A", "B", 5],
    ["A", "C", 13],
    ["A", "E", 15],
    ["B", "A", 5],
    ["B", "C", 10],
    ["B", "D", 8],
    ["C", "A", 13],
    ["C", "B", 10],
    ["C", "E", 20],
    ["C", "D", 6],
    ["D", "B", 8],
    ["D", "C", 6],
    ["E", "A", 15],
    ["E", "C", 20],
]

print_solution(prims(edges, "A"))

