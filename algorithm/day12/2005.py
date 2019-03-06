import sys
sys.stdin = open('input.txt', 'r')
# T = int(input())
# for _ in range(1,T+1):
#         N = int(input())
#         print(f'#{_}')
#         l = [1]*N
#         for i in range(N):
#                 l[i] = [1]*(i+1)
#
#         for j in range(2,N):
#                 for k in range(1,N):
#                         if k-j< 0:
#                                 l[j][j-k]=l[j-1][j-k]+l[j-1][j-1-k]
#
#         for n in l:
#                 for x in n:
#                         print(f'{x} ',end='')
#                 print()

T = int(input())
N = int(input())
for t in range(1,T+1):
    L=[[1]*n for n in range(1,N+1)]

    for i in range(2, N):
        for j in range(1, N):
            if j < i:
                L[i][i-j]=L[i-1][i-j]+L[i-1][i-1-j]