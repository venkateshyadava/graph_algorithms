INF = float("inf")


def printSolution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == float("inf"):
                print("Inf", end=" ")
            else:
                print(distance[i][j], end=" ")
        print()


def floyd_warshall(nV, G):
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    printSolution(nV, distance)


G = [[0, 8, INF, 1], [INF, 0, 1, INF], [4, INF, 0, INF], [INF, 2, 9, 1]]

floyd_warshall(4, G)
