#   Created by Elshad Karimov
#   Copyright © 2021 AppMillers. All rights reserved.

# Disjoint Set in Python

from collections import defaultdict


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

    def get_sets(self):
        sets = defaultdict(list)
        for item, parent in self.parent.items():
            sets[parent].append(item)

        return list(sets.values())

    def connected(self, x, y):
        return self.find(x) == self.find(y)


vertices = ["A", "B", "C", "D", "E"]

ds = DisjointSet(vertices)
ds.union("A", "B")
# ds.union("A", "C")
# print(ds.find("A"))
# print(ds.parent)
# print(ds.rank)
# print(ds.connected("D", "B"))
# print(ds.get_sets())
