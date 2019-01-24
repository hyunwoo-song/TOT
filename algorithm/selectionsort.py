def findBiggest(arr):
    max_N = arr[0]
    for i, n in enumerate(arr):
        if max_N < n:
            max_N = n
            index_N = i

    return max_N, index_N


def selectionSort(arr):
    newarr = []
    count = 0
    while count != 5:
        max_N = findBiggest(arr)[0]
        index_N = findBiggest(arr)[1]
        newarr += [max_N]
        arr.pop(index_N)
        count += 1    
    return newarr

print(selectionSort([5, 3, 6, 2, 10]))




# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index

# def selectionSort(arr):
#     newArr=[]
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr
# print(selectionSort([5, 3, 6, 2, 10]))
