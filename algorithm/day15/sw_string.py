import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N, K = map(int, input().split())
    List = []
    result = 0
    for n in range(N):
        List.append(list(map(int, input().split())))
        count = 0
        for i in range(N):
            if List[n][i] == 1:
                count +=1
                if i==(N-1) and count == K:
                    result += 1
                    count = 0

            else:
                if count == K:
                    result += 1
                count = 0

    NList = list(map(list, zip(*List[::-1])))
    for j in range(N):
        count = 0
        for k in range(N):
            if NList[j][k] == 1:
                count += 1
                if k == (N - 1) and count == K:
                    result += 1
                    count = 0
            else:
                if count == K:
                    result += 1
                count = 0
    print('#{} {}'.format(t, result))