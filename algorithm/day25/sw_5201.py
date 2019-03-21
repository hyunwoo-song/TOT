import sys
sys.stdin = open('5201.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    Arr_N = list(map(int,input().split()))
    Arr_M =list(map(int, input().split()))

    Arr_N = sorted(Arr_N)[::-1]
    Arr_M = sorted(Arr_M)[::-1]
    sum_Arr = 0
    for i in range(len(Arr_N)):
        for j in range(len(Arr_M)):
           if Arr_N[i] <= Arr_M[j]:
               Arr_M.pop(0)
               sum_Arr += Arr_N[i]
               break
    print('#{} {}'.format(tc, sum_Arr))
