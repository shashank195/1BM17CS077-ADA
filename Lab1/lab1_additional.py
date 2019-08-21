def find_key_data(arr, n, key):
    lowerBound, upperBound, frequency = -1, -1, 0
    l, h = 0, n

    while l <= h:
        mid = int((l+h)/2)
        if arr[mid] == key:
            frequency = frequency + 1
            if mid < lowerBound:
                lowerBound = mid
            if mid > upperBound:
                upperBound = mid
        elif arr[mid] < key:
            l = mid + 1
        else:
            h = mid - 1


n = int(input("Enter the number of elements"))
arr = []
for i in range(0,n):
    ele = int(input("Enter number"))
    arr.append(ele)
key = int(input("Enter key"))

print(find_key_data(arr, n, key))
