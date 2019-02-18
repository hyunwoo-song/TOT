import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    aj = list(map(int, input().split()))
    max_sum = 0
    min_sum = 0x7FFFFFFF
    sum_number = 0
    for i in range(N-M+1):
        sum_number = sum(aj[i:i+M])
        if max_sum < sum_number:
            max_sum = sum_number
        if min_sum > sum_number:
            min_sum = sum_number
        result= max_sum - min_sum

    print(f'#{t} {result}')