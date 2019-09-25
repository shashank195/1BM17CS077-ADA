# queens(n) = 4
# chessboard size(n*n) = 16
# k rows, i columns

n, k = 4, 0
x = [-1]*n

def NQueens(n,k):
    if k == n:
        print(x[0:n])
        return
    for i in range(n):
        if place(k,i):
            x[k] = i            
            NQueens(n,k+1)
            x[k] = -1
    return

def place(k, i):
    for j in range(k):
        if x[j] == i or abs(x[j] - i) == abs(j-k):
            return False
    return True

print(x)

NQueens(n,k)
print(x)

