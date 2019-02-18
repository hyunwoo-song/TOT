import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용


N = int(input())
for n in range(N):
    counts = []
    count = 0
    jip = list(map(int, input()))
    for i in range(1, N-1):
        if jip[0][i] == 1:
            if jip[0][i-1:i+1] ==



