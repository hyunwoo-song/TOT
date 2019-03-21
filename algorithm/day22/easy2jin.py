import sys
sys.stdin=open('easy2jin.txt', 'r')
P ={
    0:'0001101',
    1:'0011001',
    2:'0010011',
    3:'0111101',
    4:'0100011',
    5:'0110001',
    6:'0101111',
    7:'0111011',
    8:'0110111',
    9:'0001011'
}


T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    Arr= [list(map(str, input().split())) for n in range(N)]
    result = ''
    _ = 0
    z=0
    Result = ''
    for _ in range(N-6):
        i = M-1

        while 5 < i:
            for k, v in P.items():
                if Arr[_][0][i-7:i] == v and Arr[_+1][0][i-7:i] == v and Arr[_+2][0][i-7:i] == v and Arr[_+3][0][i-7:i] == v and Arr[_+4][0][i-7:i] == v:
                    i -= 6
                    result += str(k)

                    z = 1
            i -= 1
        for r in range(len(result)-1,-1,-1):
            Result += result[r]


        if z:
            break

    sum_r = 0
    S= 0


    for r1 in range(len(Result)-2,-1,-2):
        sum_r += int(Result[r1])*3

    for r2 in range(len(Result)-3, -1, -2):
        sum_r += int(Result[r2])
    sum_r += int(Result[-1])

    if not int(sum_r) % 10:
        for s in Result:
            S += int(s)
    print('#{} {}'.format(t,S))
