import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    P, Q, R, S, W =map(int, input().split())
    A = P * W
    result = A

    if R < W:
        B = Q + S*(W-R)
    else:
        B = Q

    if A >= B:
        result = B
    print(f'#{t} {result}')