T = int(input())
for _ in range(T):
    S = input()
    if S == S[::-1]:
        print(f'#{_+1} 1')
    else:
        print(f'#{_+1} 0')