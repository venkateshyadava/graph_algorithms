class DisjointSet:
    def __init__(self, vertices):
        self.parents = {}
        for i in vertices:
            self.parents[i] = i
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, vertex):
        while self.parents[vertex] != vertex:
            vertex = self.parents[vertex]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parents[yroot] = xroot
            self.rank[xroot] += 1

