import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용


T = int(input())
for t in range(1, T+1):
    N = int(input())
    l = list(map(int, input().split()))
    new_l = sorted(l)
    bin = []
    a = len(l) - 1
    b = 0
    count = 10
    for i in range(len(l)):
        while count > 0:
            if a > b:
                bin.append(new_l[a])
                a -=1
                bin.append(new_l[b])
                b +=1
                count -= 2
    k = ' '.join(map(str, bin))
    print(f"#{t} {k}")