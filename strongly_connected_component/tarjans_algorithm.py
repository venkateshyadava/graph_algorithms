from collections import defaultdict


def strongly_connected_components(graph):

    index_counter = [0]
    stack = []
    result = []
    low_links = {}
    index = {}

    def tarjan(node):

        index[node] = index_counter[0]
        low_links[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)

        try:
            successors = graph[node]
        except:
            successors = []
        for successor in successors:
            if successor not in low_links:
                tarjan(successor)
                low_links[node] = min(low_links[node], low_links[successor])
            elif successor in stack:
                low_links[node] = min(low_links[node], index[successor])

        if low_links[node] == index[node]:
            connected_component = []
            while True:
                successor = stack.pop()
                connected_component.append(successor)
                if successor == node:
                    break
            component = tuple(connected_component)
            result.append(component)

    for node in graph:
        if node not in low_links:
            tarjan(node)

    return result


test_graph = {
    "A": ["B"],
    "B": ["D", "E", "C"],
    "C": ["G"],
    "D": ["A", "E"],
    "E": ["F"],
    "F": ["C", "G", "E"],
    "G": ["C"],
}

print(strongly_connected_components(test_graph))