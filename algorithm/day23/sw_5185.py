import sys
sys.stdin = open('5185.txt', 'r')

T= int(input())
for t in range(1,T+1):
    result = ''
    N, Num = map(str, input().split())
    Num =bin(int(Num, 16))[2::]
    result = str(Num)
    while len(result) < int(N)*4:
        result = '0' + result
    print('#{} {}'.format(t, result))
