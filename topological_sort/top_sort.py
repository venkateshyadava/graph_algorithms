from collections import defaultdict


class Graph:
    def __init__(self, number_of_vertices):
        self.graph = defaultdict(list)
        self.number_of_vertices = number_of_vertices

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def top_sort_util(self, vertex, visited, stack):
        visited.append(vertex)
        for adjacent in self.graph[vertex]:
            if adjacent not in visited:
                self.top_sort_util(adjacent, visited, stack)

        stack.append(vertex)

    def top_sort(self):

        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.top_sort_util(k, visited, stack)

        return stack[::-1]


customGraph = Graph(8)
customGraph.add_edge("A", "C")
customGraph.add_edge("C", "E")
customGraph.add_edge("E", "H")
customGraph.add_edge("E", "F")
customGraph.add_edge("F", "G")
customGraph.add_edge("B", "D")
customGraph.add_edge("B", "C")
customGraph.add_edge("D", "F")

print(customGraph.top_sort())
