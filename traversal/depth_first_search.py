from collections import defaultdict


class Graph:
    def __init__(self):
        self.gdict = defaultdict(list)

    def insert(self, vertex, edge):
        self.gdict[vertex] = edge

    def dfs_util(self, visited, node):
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbour in self.gdictgraph[node]:
                self.dfs(visited, neighbour)

    def dfs(self, vertex):
        visited = []
        self.dfs_util(visited, vertex)
