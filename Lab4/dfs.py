def dfs(v):
    print(v)
    visited[v] = 1
    for i in range(4): # to number of nodes
        if adjacency_matrix[v][i] == 1 and visited[i] == 0:
            dfs(i)

n = 4 # number of nodes
visited = []
# adjacency_matrix = [[0,0,0,1], [0,0,0,1], [0,0,0,1], [1,1,1,0]]
adjacency_matrix = [[0,1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]]

for i in range(n):
    visited.append(0)

dfs(1)s