def k_smallest_element(arr, n, k):
    for i in range(k):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

    return arr[k-1]


n = int(input("Enter number of elements you want"))
arr = []

for i in range(n):
    x = int(input("Enter number"))
    arr.append(x)

k = int(input("Enter value of k"))

print(k_smallest_element(arr, len(arr), k))