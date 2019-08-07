def binary_search(num_array, n, key) -> int:
    low = 0
    high = n
    while low<=high:
        mid=int((low+high)/2)
        if key == num_array[mid]:
            return 1
        elif key < num_array[mid]:
            high = mid - 1
        elif key > num_array[mid]:
            low = mid + 1
    return -1

result = binary_search([1,5,7], 3, 0)
print("Result:", result)