def GGG(IN,POST,start, end):
    if POST[end] in Top:
        return

    if start >= end:
        Top.append(POST[end])
        return

    if start - end ==1:
        Top.append(POST[end])
        return

    if start - end ==-1:
        Top.append(POST[start])
        return

    for i in range(N):
        if IN[i] == POST[end]:
            Top.append(IN[i])
            if i == N-1:
                i = N -2
            break



    GGG(IN,POST,start,i-1)
    GGG(IN,POST,i,end-1)


N = int(input())
In_O = list(map(int, input().split()))
Post_O = list(map(int, input().split()))
Top =[]
GGG(In_O,Post_O,0, N-1)
print(*Top)