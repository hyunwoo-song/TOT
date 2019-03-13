import sys
sys.stdin = open('bj_1517.txt', 'r')

def MERGE(l,r):
    global count
    i=0
    j=0
    Result = [0]*(len(l)+len(r))
    z= 0
    while i < len(l)and j < len(r):
        if l[i] > r[j]:
            Result[z]=r[j]
            j += 1
            z += 1
            count += 1
        else:
            Result[z]=l[i]
            i += 1
            z += 1



    if i == len(l):
        for k in range(j,len(r)):
            Result[z]=r[k]
            z+=1
    else:
        for q in range(i, len(l)):
            Result[z] = l[q]
            z += 1

    return Result



def MERGE_SORT(List):
    global count
    if len(List) <= 1:
        return List

    m = len(List) // 2
    Left = List[:m]
    Right = List[m:]

    Left = MERGE_SORT(Left)
    Right = MERGE_SORT(Right)


    return MERGE(Left,Right)

N= int(sys.stdin.readline())
Data = list(map(int, sys.stdin.readline().split()))
count = 0
R = MERGE_SORT(Data)
Count = []

for w in range(len(R)):
    o = 0
    while R[w] != [o]:
        o += 1
    Count.append(o)
print((sum(Count)//2-2)*2)