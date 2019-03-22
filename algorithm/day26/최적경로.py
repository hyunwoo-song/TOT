import sys
sys.stdin = open('input.txt')

def Go(num):
    global N,result,cnt,low
    Visited[num] =True
    Here=[Arr[num][0],Arr[num][1]]

    if low < result:
        return

    if cnt == N:
        result += abs(Arr[-1][0] - Here[0]) + abs(Arr[-1][1] - Here[1])
        if low > result:
            low = result
        Result.append(result)
        result -= abs(Arr[-1][0] - Here[0]) + abs(Arr[-1][1] - Here[1])

        return

    for i in range(1,N+1):
        if not Visited[i]:

            result += abs(Arr[i][0]-Here[0]) +abs(Arr[i][1]-Here[1])
            cnt+=1
            Go(i)
            Visited[i] =False

            result -= abs(Arr[i][0]-Here[0]) +abs(Arr[i][1]-Here[1])

            cnt -= 1

TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    L = list(map(int, input().split()))
    Arr =[[L[1],L[0]]]
    for l in range(4,len(L),2):
        Arr.append([L[l+1],L[l]])
    Hom = [L[3], L[2]]
    Arr.append(Hom)
    low =0x7FFFFFFF
    cnt =0
    result = 0
    Result = []
    Visited = [0] *(N+2)
    Go(0)
    print('#{} {}'.format(tc, min(Result)))





