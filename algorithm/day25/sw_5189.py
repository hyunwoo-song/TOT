import sys
sys.stdin = open('5189.txt')


def Go(num):
    global N,result,cnt
    Visited[num] =True

    if cnt == N-1:
        result += Arr[num][0]
        Result.append(result)
        result -= Arr[num][0]

        return

    for i in range(N):
        if not Visited[i]:
            result += Arr[num][i]
            cnt+=1
            Go(i)
            Visited[i] =False
            result -= Arr[num][i]
            cnt -= 1





T= int(input())
for tc in range(1, T+1):
    N= int(input())
    Arr = [list(map(int, input().split())) for n in range(N)]
    l=[j for j in range(1,N+1)]
    Visited = [0] * N
    Result=[]
    result = 0
    cnt = 0
    Go(0)
    print('#{} {}'.format(tc, min(Result)))
