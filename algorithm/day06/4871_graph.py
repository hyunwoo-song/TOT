import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
def Cham(S,G):
    global E,  result
    K=[]
    if result:
        return
    else:
        if Mymap[S][G]:
            result =1

        else:
            for e in range(1, E + 1):
                if Mymap[S][e]:
                    K += [e]
            for k in K:
                S = k
                Cham(S, G)

    return

for t in range(1, T+1):
    V, E = map(int, (input().split()))
    Mymap = [[0] * (V+1) for v in range(V+1)]
    l = []
    result = 0

    for e in range(E):
        l.append(list(map(int, input().split())))
    S, G = map(int, (input().split()))


    for e in range(0, E):
        y=l[e][0]
        x=l[e][1]
        Mymap[y][x] =1
    Cham(S, G)
    print(f'#{t} {result}')





















    #
    # 두
    # 개의
    # 노드에
    # 대해
    # 경로가
    # 있으면
    # 1, 없으면
    # 0