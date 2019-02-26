import sys
sys.stdin=open('input.txt', 'r')


def Fire(list):
    while Que[0]:
        Que.append(Que.pop(0) // 2)
        num.append(num.pop(0))

    if not Que[0]:
        Que.pop(0)
        num.pop(0)
        return


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    Pizza = list(map(int, input().split()))
    Que = []
    num = []
    m = 0

    while m != M:
        if len(Que) < N:
            Que.append(Pizza[m]//2)
            num.append(m + 1)
            m += 1
        else:
            Fire(Que)

    while len(Que) != 1:
        Fire(Que)

    print(f'#{t} {num[0]}')