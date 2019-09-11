def enqueue(n):
    queue.append(n)

def dequeue():
    queue.pop(0)

def bfs(k):
    visited[k] = 1
    enqueue(k)
    while queue:
        poppedItem = dequeue()
        for i in adjacencyMatrix[poppedItem]:
            if visited[i] == 0:
                enqueue(i)
                visited[i] = 1
                print(i)

adjacencyMatrix = [[1,1,1,0], [1,0,0,0], [1,1,1,0], [0,0,0,1]]
visited = [0,0,0,0]
n = 4
sourceVertex = 3
queue = []

print(bfs(sourceVertex))
