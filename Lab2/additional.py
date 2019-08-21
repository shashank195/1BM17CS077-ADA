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

def search_element(arr, key):
    pivot = arr.index(max(arr))
    if key >= arr[0]:
        return binary_search(arr[:pivot+1], key)
    else:
        return binary_search(arr[pivot+1:], key)

print(search_element([3,4,5,1,2], 6))