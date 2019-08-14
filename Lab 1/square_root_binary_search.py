def compute_square_root(n):
    low, high = 0, n
    root = 0
    while low <= high:
        mid = int((low+high)/2)
        mid_square = mid*mid
        if mid_square == n:
             return mid
        elif mid_square < n:
            root = mid
            low = mid + 1
        else:
            high = mid - 1
    return root

print(compute_square_root(1))