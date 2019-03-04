import sys
sys.stdin = open('input.txt', 'r')

def RMM(Strings):
    global result
    for n in range(N):
        Count = 0
        for i in range(M // 2):
            if Strings[n][i] == Strings[n][(M - 1) - i]:
                Count += 1
                if Count == M // 2:
                    result = ''.join(Strings[n][:i:])
            else:
                break

    else:
        Strings = list(map(list, zip(*Strings[::-1])))
        return RMM(Strings)




T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Strings = []
    for n in range(N):
        Strings.append(list(map(str, input())))
    result = ''
    S =[]

    RMM(Strings)

    print('#%d %s' %(t ,result))