import sys
sys.stdin = open('ex3')


def Per(num,cnt,result):
    global N, Result
    Visited[num] = 1
    Y = abs(Cookie[2*num] - Robot[2*cnt])
    X = abs(Cookie[2*num+1]- Robot[2*cnt+1])
    cnt += 1

    if Result <= result:
        return

    if cnt == N:
        if Result > result+Y+X:
            Result =result+Y+X
            return

    for i in range(N):
        if not Visited[i]:
            Per(i,cnt,result+Y+X)
            Visited[i] = 0


TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    Cookie = list(map(int,input().split()))
    Robot = list(map(int,input().split()))
    Result = 0x7FFFFFFF
    Visited = [0] * N
    for j in range(N):
        result = 0
        Per(j,0,result)
        Visited[j] = 0
    print('#{} {}'.format(tc, Result))