def binary_search(num_array, key) -> int:
    low = 0
    high = len(num_array)-1
    while low <= high:
        mid =int((low+high)/2)
        if key == num_array[mid]:
            return 1
        elif key < num_array[mid]:
            high = mid - 1
        elif key > num_array[mid]:
            low = mid + 1
    return -1

def findPivot(arr, low, high):
    if high < low: 
        return -1
    if high == low:
        return low
    mid = int((low+high)/2)

    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    
    if mid > low and arr[mid] < arr[mid-1]:
        return mid-1
    
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid-1)
    return findPivot(arr, mid+1, high)


def search_element(arr, key):
    # pivot = arr.index(max(arr))
    pivot = findPivot(arr, 0, len(arr)-1)
    if key >= arr[0]:
        return binary_search(arr[:pivot+1], key)
    else:
        return binary_search(arr[pivot+1:], key)

print(search_element([3,4,5,1,2], 2))