import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용




T = int(input())
for t in range(1, T+1):
    N = int(input())
    Data = list(map(int, input().split()))

    my_max = Data[0]
    my_min = Data[-1]
    result = 0
    for v in Data:
        if my_max < v:
            my_max = v
        if my_min > v:
            my_min = v
        result = my_max - my_min
    print('#{} {}'.format(t, result))
