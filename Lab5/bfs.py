def enqueue(n):
    queue.append(n)

def dequeue():
    return queue.pop(0)

def bfs(k, queue):
    visited[k] = 1
    enqueue(k)
    while queue:
        poppedItem = dequeue()
        for i in range(len(adjacencyMatrix[poppedItem])):
            if i == 1:
                if visited[i] == 0:
                    enqueue(i)
                    visited[i] == 1
                    print(i)

adjacencyMatrix = [[0,1,1,1,0,0], [1,0,1,0,1,0], [1,1,0,0,0,0],[1,0,0,0,1,1], [0,1,0,1,0,1], [0,0,0,1,1,0]]
visited = [0,0,0,0]
n = 6
sourceVertex = 0
queue = []

print(bfs(sourceVertex, queue))
