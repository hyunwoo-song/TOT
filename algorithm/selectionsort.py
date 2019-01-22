def findBiggest(arr):
    biggest = arr[-1]
    for i in arr:
        if i > biggest:
            biggest = i 
    return biggest
print(biggest)

def selectionSort(arr):
    newArr = []
    count = 0
    while count == len(arr):
        for i in arr:
            biggest = findBiggest(arr)
            newArr.append(i)
            count += 1
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))