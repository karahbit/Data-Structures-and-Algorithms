#   Created by Elshad Karimov
#   Copyright © 2021 AppMillers. All rights reserved.


from collections import deque


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        queue = deque([start])
        while queue:
            print(queue)
            path = queue.popleft()
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


customDict = {
    "a": ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"],
}

g = Graph(customDict)
print(g.bfs("a", "f"))
