from math import sqrt

def solveSudoku(grid):
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 0:
                for i in range(1,5):
                    if isSafe(grid, i, row, col):
                        grid[row][col] = i
                        if solveSudoku(grid):
                            return True
                        grid[row][col] = 0
    return False

def isSafe(grid, num, row, col):
    return not usedInRow(grid, num, row) and not usedInCol(grid, num, col) and not usedinBox(grid, num, row-row%int(sqrt(n)), col-col%int(sqrt(n)))
# row - row %sqrt(n) returns start index of subgrid's row

def usedInRow(grid, num, row):
    for col in range(n):
        return grid[row][col] == num
    return False

def usedInCol(grid, num, col):
    for row in range(n):
        return grid[row][col] == num
    return False

def usedinBox(grid, num, boxStartRow, boxStartCol):
    for row in range(int(sqrt(n))):
        for col in range(int(sqrt(n))):
            return grid[row+boxStartRow][col+boxStartCol] == num
    return False

#4x4 grid
n = 4
grid = [[2,0,0,0], 
        [0,1,3,0],
        [3,0,0,1], 
        [0,2,4,0]]

print(solveSudoku(grid))


