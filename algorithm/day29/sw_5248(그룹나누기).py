import sys
sys.stdin = open('5248.txt')

def Find_Set(num):
    if num == P[num]:
        return num
    else:
        return Find_Set(P[num])
def Uninon(x, y):
    P[Find_Set(x)] = Find_Set(y)

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int,input().split())
    Arr = list(map(int,input().split()))
    P=[i for i in range(N+1)]
    for j in range(0,len(Arr),2):
        a= Arr[j]
        b = Arr[j+1]
        Uninon(a,b)

    for i in range(1, N + 1):
        P[i]=Find_Set(i)

    result = len(set(P))-1
    print('#{} {}'.format(tc, result))

