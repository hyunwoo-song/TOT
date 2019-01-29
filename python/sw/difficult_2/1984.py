T = int(input())
for _ in range(T):
    l = list(map(int, input().split()))
    l.sort()
    l.pop(0)
    l.pop(-1)
    sum_l =0
    for i in l:
        sum_l += i
    avg_l = sum_l / len(l)
    avg_l = round(avg_l, 0)
    print(f'#{_+1} {int(avg_l)}')