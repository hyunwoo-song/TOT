import sys
sys.stdin = open('joon.txt')
from math import factorial

def CHOO(num,left,right):
    global cnt, result, ssum, N, flag

    if right > left:
        return

    if cnt == N:
        result += 1
        return

    if left >= ssum - left:
        result += 2**(N-cnt)*factorial(N-cnt)
        return

    for j in range(N):
        if not Visited[j]:
            Visited[j]= 1
            cnt += 1
            CHOO(num,left+Kg[j],right)
            CHOO(num,left,right+Kg[j])
            cnt -= 1
            Visited[j]=0


TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    Kg = list(map(int,input().split()))
    result = 0
    ssum = sum(Kg)

    for i in range(N):
        left = 0
        right = 0
        Visited = [0] * N
        Visited[i]= 1
        left = Kg[i]
        cnt =1
        CHOO(i,left,0)
        Visited[i] = 0

    print('#{} {}'.format(tc, result))
