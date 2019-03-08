import sys
sys.stdin = open('zip.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N= int(input())
    result = ''
    for n in range(N):
        Ci, Ki =map(str, input().split())

        result += Ci*int(Ki)
    print('#{}'.format(t))
    R=list(result)
    result2 = ''
    count=0
    for r in range(len(R)):
        if count != 10:
            result2 += R[r]
            count +=1
        elif count == 10:
            print(result2)
            result2 = ''
            result2 += R[r]
            count = 1

        if r == len(R)-1:
            print(result2)
            count = 1