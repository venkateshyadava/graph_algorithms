from collections import defaultdict


class Graph:
    def __init__(self):
        self.gdict = defaultdict(list)

    def insert(self, vertex, edge):
        self.gdict[vertex] = edge

    def dfs(self, vertex):
        traversal = []
        stack = []
        visited = []
        stack.append(vertex)
        visited.append(vertex)

        def dfs_util(vertex):
            nonlocal traversal, stack, visited
            curr_vertex = stack.pop()
            for neighbors in self.gdict[curr_vertex]:
                if neighbors not in visited:
                    traversal.append(curr_vertex)
                    dfs_util(neighbors)

        return traversal
