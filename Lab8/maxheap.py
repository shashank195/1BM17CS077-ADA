arr = [0,90,15,10,7,12,2]
# arr = [0, 9,15,10,7,12,11]

def checkMaxHeap(arr):
    for i in range(1, (len(arr)//2)):
        if arr[i] >= max(arr[2*i], arr[2*i+1]):
            continue
        else:
            return False
    return True

print(checkMaxHeap(arr))