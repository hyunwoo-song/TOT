T = int(input())
for t in range(T):
    l = list(map(int, input().split()))
    hour = (l[0]+l[2]) % 12
    minute = (l[1]+ l[3]) % 60
    mok = (l[1]+ l[3]) // 60
    print(f'#{t+1} {hour+mok} {minute}')