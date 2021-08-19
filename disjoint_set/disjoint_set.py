class DisJointSet:
    def __init__(self, vertices):
        self.rank = [0 for _ in vertices]
        self.parent = [i for i in vertices]

    def find(self, vertex1):
        node = vertex1
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]

        return node

    def union(self, vertex1, vertex2):
        if self.find(vertex1) == self.find(vertex2):
            return

        if self.rank[vertex1] > self.rank[vertex2]:
            self.parent[vertex2] = self.parent[vertex1]
        elif self.rank[vertex2] > self.rank[vertex1]:
            self.parent[vertex1] = self.parent[vertex2]
        else:
            self.rank[vertex1] += 1
            self.parent[vertex2] = self.parent[vertex1]


d = DisJointSet([0, 1, 2, 3, 4, 5, 6, 7])

print(d.find(1))
print(d.find(2))
d.union(1, 2)
d.union(1, 3)
d.union(1, 5)
print(d.find(2))
print(d.find(5))
