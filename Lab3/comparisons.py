def selection_sort(arr, n):
    count = 0
    for i in range(n):
        min = i
        for j in range(i+1, n):
            count += 1
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

    return count

def bubble_sort(arr, n):
    count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            count += 1
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return count


def split(a, low, high):
    if low < high:
        middle = (low+high)//2
        split(a, low, middle)
        split(a, middle+1, high)
        combine(a, low, middle, high)


def combine(a, low, middle, high):
    i = low
    j = middle+1
    c = []
    while i <= middle and j <= high:
        if a[i] < a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1

    if i > middle:
        while j <= high:
            c.append(a[j])
            j += 1
    if j > high:
        while i <= middle:
            c.append(a[i])
            i += 1 
            
    for i in range(low, high+1):
        a[i] = c[i-low]

arr = [1,3,2,5]
print(selection_sort(arr, 4))
print(bubble_sort(arr,4))
split(arr, 0, len(arr)-1)
