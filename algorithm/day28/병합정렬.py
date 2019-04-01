import sys
sys.stdin = open('input.txt')

def MERGE(left, right):
    global count
    i = 0
    j = 0
    Arr = []

    if left[-1] > right[-1]:
        count += 1

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            Arr.append(left[i])
            i += 1

        else:
            Arr.append(right[j])
            j += 1

    while (i<len(left)):
        Arr.append(left[i])
        i+= 1

    while (j<len(right)):
        Arr.append(right[j])
        j+= 1

    return Arr


def MS(L):

    if len(L) <=1:
        return L

    mid = len(L)//2
    Left = L[:mid]
    Right = L[mid:]


    return MERGE(MS(Left), MS(Right))





TC = int(input())
for tc in range(1, TC+1):
    count = 0

    N = int(input())
    Aj=list(map(int, input().split()))
    print('#{} {} {}'.format(tc, MS(Aj)[N//2],count//2))