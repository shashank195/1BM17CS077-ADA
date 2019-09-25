# queens(n) = 4
# chessboard size(n*n) = 16
# k rows, i columns

n, k = 4, 0
x = [-1]*(n)

def NQueens(n,k):
    for i in range(n):
        if place(k,i):
            x[k] = i
            if k == n:
                print(x[1:n])
            else:
                NQueens(n,k+1)

def place(k, i):
    for j in range(1, k):
        if x[j] == i or abs(x[j] - i) == abs(j-k):
            return False
    return True

print(x)

NQueens(n,k)
print(x)

