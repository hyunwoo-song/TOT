import sys
sys.stdin= open('5186.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = input()
    N=float(N)
    k = 0.5
    result = ''
    while True:
        if N < k:
            k /= 2
            result +='0'
        else:
            N -= k
            k /= 2
            result += '1'

        if len(result) >=13:
            result= 'overflow'
            break
        elif N == 0:
            break

    print('#{} {}'.format(t,result))