from collections import defaultdict

adjacency = [[0,1,1,0], [0,0,1,0], [1,0,0,1], [0,0,0,1]]

def convertAdjacencyMatrixToDictionary(matrix):
    d = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                d[i].append(j)
    return d


print(convertAdjacencyMatrixToDictionary(adjacency))