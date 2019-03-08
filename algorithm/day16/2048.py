import sys
sys.stdin = open('2048.txt', 'r')


def LEFT(Arr):
    global Ni
    for n in range(Ni):
        k = 1
        while k < Ni:
            if Arr[n][k]==Arr[n][k-1]:
                Arr[n][k-1] = Arr[n][k-1] + Arr[n][k]
                Arr[n][k]=0
                Arr[n].append(Arr[n].pop(k))

            elif Arr[n][k-1] == 0:
                Arr[n][k-1]=Arr[n][k]
                Arr[n].append(Arr[n].pop(k))


            else:
                Arr[n][k]=Arr[n][k]
                Arr[n][k-1]=Arr[n][k-1]

            k += 1


T= int(input())
for t in range(1,T+1):
    N, S = map(str, input().split())
    Arr=[]
    for n in range(int(N)):
        Arr.append(list(map(int, input().split())))
        Ni = int(N)


    if S == 'left':
        W=0

    elif S == 'up':
        W=3

    elif S == 'right':
        W=2

    else:
        W=1


    for w in range(W):
        Arr = list(map(list, zip(*Arr[::-1])))

    List=[]
    for ni in range(Ni):
        for z in range(Ni):
            if Arr[ni][z]:
                List.append(Arr[ni][z])


    LEFT(Arr)
    for w2 in range(4-W):
        Arr = list(map(list, zip(*Arr[::-1])))

    print('#{}'.format(t))
    for _ in range(Ni):
        print(*Arr[_])