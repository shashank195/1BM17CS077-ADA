print("Enter numbers in array")

def set_integers():
    num_array = list()
    num = input("Enter how many elements you want:")

    for i in range(int(num)):
        n = input("num :")
        num_array.append(int(n))
    return num_array

def max_integer(num_list) -> int:
    max = 0
    for index, num in enumerate(num_list):
        if max < num:
            max = num
    return max
    
num_array = set_integers()
max = max_integer(num_array)
print(max)