import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용


def chill(x1, y1, x2, y2, c):
    for dx in range(x1,x2+1):
        for dy in range(y1, y2+1):
            if bin[dx][dy]== 0:
                bin[dx][dy] = c
            elif bin[dx][dy]== 1:
                if c == 2:
                    bin[dx][dy] = 3

            elif bin[dx][dy]== 2:
                if c == 1:
                    bin[dx][dy] = 3
    return bin


T = int(input())

for t in range(1, T+1):
    N = int(input())
    colors = []
    bin = [[0]*10 for i in range(10)]
    result = 0
    count = 0
    for n in range(N):
        colors.append(list(map(int, input().split())))

    len_c = len(colors)
    for c in range(len_c):
        result = chill(colors[c][0], colors[c][1], colors[c][2], colors[c][3], colors[c][4])
    for dx in range(10):
        for dy in range(10):
            if bin[dx][dy] == 3:
                count += 1
    print(f'#{t} {count}')
