import sys
sys.stdin = open('all.txt')

TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())

    A= list(map(int, input().split()))
    B = list(map(int, input().split()))
    Vote=[0]*(N+1)
    for i in range(len(B)):
        j = 0
        while B[i] < A[j]:
            j += 1
        Vote[j] += 1

    result =Vote.index(max(Vote)) + 1
    print('#{} {}'.format(tc, result))

