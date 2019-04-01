import sys
sys.stdin = open('5247.txt')

def CAL(x,y):
    global cnt,result
    if x in Q:
        return

    if result <= cnt:

        return

    if y == x:
        result = cnt
        return

    if x < 0:
        return

    for i in range(4):
        if i == 0:
            cnt += 1
            CAL(x+1, y)
            cnt -= 1
        elif i == 1:
            cnt += 1
            CAL(x - 1, y)
            cnt -= 1
        elif i==2:
            cnt += 1
            CAL(x*2, y)
            cnt -= 1
        else:
            cnt += 1
            CAL(x -10, y)
            cnt -= 1


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    cnt =0
    K=M
    Q=[]
    result =0
    while K > N:
        if K %2:
            if K-1 >=N:
                K -= 1
                result +=1

            else:
                break
        else:
            if K//2 >= N:
                K //= 2
                result += 1

            else:
                break

    result = result+9


    CAL(N,M)
    print('#{} {}'.format(tc,result))