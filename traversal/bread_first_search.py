from collections import defaultdict


class Graph:
    def __init__(self):
        self.gdict = defaultdict(list)

    def insert(self, vertex, edge):
        self.gdict[vertex] = edge

    def bfs(self, vertex):
        q = []
        visited = []
        traversal = []
        q.append(vertex)
        visited.append(vertex)

        while q:
            curr_vertex = q.pop(0)
            traversal.append(curr_vertex)
            for neighbor in self.gdict[curr_vertex]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    q.append(neighbor)
        return traversal
