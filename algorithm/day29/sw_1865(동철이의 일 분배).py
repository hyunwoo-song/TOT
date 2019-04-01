import sys
sys.stdin = open('1865.txt')

def Go(num):
    global N,result,cnt
    Visited[num] =True

    if cnt == N-1:
        result += P[num][0]
        Result.append(result)
        result -= P[num][0]

        return

    for i in range(N):
        if not Visited[i]:
            result *= P[num][i]
            cnt+=1
            Go(i)
            Visited[i] =False
            result -= P[num][i]
            cnt -= 1

TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    P = [list(map(int,input().split())) for n in range(N)]
    Visited = [0]*N

    Result=[]
    result = 1
    cnt = 0
    Go(0)
    print('#{} {}'.format(tc, min(Result)))