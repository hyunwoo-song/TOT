import sys
sys.stdin=open('Quick.txt')

def Quick_Sort(L,start,end):
    if start >= end:
        return

    if abs(start - end) == 1:
        if L[start] < L[end]:
            return
    Pivot = L[start]

    i = start
    j = end
    while j <= end:
        while L[i] <= Pivot:
            i += 1

            if i > end:
                break
        if j <= end:
            while L[j] > Pivot:
                j -= 1
                if i >= j:
                    break
        if i >= j:
            break

        if j <= end and i <=end:
            L[j], L[i] = L[i], L[j]
    i -= 1
    L[start], L[i] = L[i], L[start]

    if i > 0:
        Quick_Sort(L,0,i-1)
    Quick_Sort(L,i+1,end)




TC = int(input())
for tc in range(TC):
    Arr = list(map(int, input().split()))
    Arr[0], Arr[len(Arr) // 2] = Arr[len(Arr) // 2], Arr[0]
    Quick_Sort(Arr, 0, (len(Arr)-1))
for i in range(len(Arr)):
    print(i)




