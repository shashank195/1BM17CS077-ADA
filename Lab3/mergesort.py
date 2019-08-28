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
        


a = [5,4,3,2,1]

print(len(a)-1)
split(a, 0, len(a)-1)


print(a)