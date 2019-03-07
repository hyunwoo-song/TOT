import sys
sys.stdin = open('input.txt', 'r')

def Pick(y,x):
    global M, sum_map
    for dy in range(M):
        for dx in range(M):
            sum_map += Arr[y+dy][x+dx]
    Map.append(sum_map)
    sum_map = 0
    return




T= int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Arr = [list(map(int, input().split())) for n in range(N)]
    sum_map = 0
    Map = []
    P = N-M

    for y in range(P+1):
        for x in range(P+1):
            Pick(y,x)

    result = max(Map)
    print('#{} {}'.format(t, result))
