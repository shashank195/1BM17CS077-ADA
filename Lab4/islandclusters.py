def dfs(i,j):
    rowNbr = [-1,-1,-1,0,0,1,1,1]
    colNbr = [-1,0,1,-1,1,-1,0,1]

    visited[i][j] = 1

    for k in range(8): # to number of possible nodes around given vertex
        if isSafe(i+rowNbr[k],j+colNbr[k]):
            dfs(i+rowNbr[k],j+colNbr[k])

def isSafe(i,j):
    return i>=0 and j>=0 and i<len(matrix) and j<len(matrix[0]) and matrix[i][j] == 1 and visited[i][j] == 0

def findClusters(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                dfs(i,j)
                count+=1
    return count

matrix = [[1,0,1,0,1], [1,1,0,0,0], [0,1,0,1,1]]
visited = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

print(findClusters(matrix))