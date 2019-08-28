def quickSort(a, low, high):
    if low < high:
        pivot_pos = partition(a, low, high)
        quickSort(a, low, pivot_pos-1)
        quickSort(a, pivot_pos+1, high)

def partition(a, low, high):
    pivot = a[low]
    i = low + 1 
    j = high
    while True:
        while a[i] <= pivot and i <= high:
            i+=1
        while a[j] > pivot and j >= low:
            j-=1
        if i < j:
            a[i], a[j] = a[j], a[i]
        else:
            a[low] = a[j]
            a[j] = pivot
            return j

    
a = [7,99,3,45,124]

quickSort(a, 0, len(a)-1)

print(a)