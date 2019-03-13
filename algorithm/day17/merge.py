def MERGE(l,r):
    i=0
    j=0
    Result = [0]*(len(l)+len(r))
    z= 0
    while i < len(l)and j < len(r):
        if l[i] > r[j]:
            Result[z]=r[j]
            j += 1
            z += 1
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
    if len(List) <= 1:
        return List

    m = len(List) // 2
    Left = List[:m]
    Right = List[m:]

    Left = MERGE_SORT(Left)
    Right = MERGE_SORT(Right)

    return MERGE(Left,Right)


Data = [38, 27, 43, 3, 9, 82, 10]

print(MERGE_SORT(Data))





