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


arr = [1,3,2,5]
print(selection_sort(arr, 4))
print(bubble_sort(arr,4))