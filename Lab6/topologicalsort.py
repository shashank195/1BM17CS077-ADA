adjacencyMatrix = [[0,1,1],
                   [0,0,1],
                   [0,0,0]]
n = 3 # number of nodes
indegree = [0]*n

def topologicalSort(matrix, n):
    for i in range(n):
        for j in range(n):
            indegree[i] = indegree[i] + matrix[j][i]    

    for i in range(n):
        j = indegree.index(0)
        print(j, end=" ")
        indegree[j] = -1
        for k in range(n):
            if matrix[j][k] == 1:
                indegree[k] = indegree[k] - 1

topologicalSort(adjacencyMatrix, n)