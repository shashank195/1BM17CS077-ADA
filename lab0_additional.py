def binary_search(num_array, n, key) -> int:
    low = 0
    high = n
    while low <= high:
        mid =int((low+high)/2)
        if key == num_array[mid]:
            return 1
        elif key < num_array[mid]:
            high = mid - 1
        elif key > num_array[mid]:
            low = mid + 1
    return -1


def read_test_case_file():
    input = open("testcase.txt")
    n = input.readlines()
    for lines in n:
        a = map(int, lines.split())

read_test_case_file()
# result = binary_search([1,5,7], 3, 0)
# print("Result:", result)

# for i in line1_testcases:
#     binarysearch(line3,line2_n,line2_key)
