class Graph:
    def __init__(self, gdict={}):
        self.gdict = gdict

    def bfs(self, start, end):
        q = []
        q.append([start])

        while q:
            path = q.pop(0)
            node = path[-1]
            if node == end:
                return path

            for adj in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adj)
                q.append(new_path)


customDict = {}


customDict = {
    "a": ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"],
}

g = Graph(customDict)
print(g.bfs("a", "e"))