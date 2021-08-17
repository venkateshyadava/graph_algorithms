class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []

    def add_edges(self, s, d, w):
        self.graph.append([s, d, w])

    def add_nodes(self, node):
        self.nodes.append(node)

    def print_solution(self, dist):
        for key, value in dist.items():
            print(" " + key, " :  ", value)

    def bellman_ford(self, src):
        dist = {i: float("inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != float("inf") and dist[s] + w < dist[d]:
                print("Negative edge exists.")

        return dist


g = Graph(5)
g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")
g.add_nodes("E")
g.add_edges("A", "C", 6)
g.add_edges("A", "D", 6)
g.add_edges("B", "A", 3)
g.add_edges("C", "D", 1)
g.add_edges("D", "C", 2)
g.add_edges("D", "B", 1)
g.add_edges("E", "B", 4)
g.add_edges("E", "D", 2)
dist = g.bellman_ford("E")
g.print_solution(dist)
