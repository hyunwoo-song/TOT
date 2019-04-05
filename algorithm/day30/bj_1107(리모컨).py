import sys
sys.stdin = open('1107.txt')

def RM(start, end):
    global cnt2,cnt3
    R = [99] * 10
    W = [99] * 10
    U = ''
    T = ''
    flag =0
    n = len(str(end))
    Z = '1'+'0'*(n)
    X = '9'*(n-1)

    for z in Z:
        b = int(z)
        if H[b]:
            U += z
            cnt2 += 1
        else:
            for h in range(len(H)):
                if H[h]:
                    flag = 2
                    R[h] = abs(h-b)
            if flag==2:
                r=R.index(min(R))
                U += str(r)
                cnt2 += 1
                flag = 0
    if U:
        cnt2 += abs(int(U) - end)

    for x in X:
        c = int(x)
        if I[c]:
            T += x
            cnt3 += 1
        else:
            for i in range(len(I)):
                if I[i]:
                    flag = 2
                    W[i] = abs(i-c)
            if flag==2:
                r=W.index(min(W))
                T += str(r)
                cnt3 += 1
                flag = 0
    if T:
        cnt3 += abs(int(T) - end)

N = int(input())
M = int(input())
List = list(map(int, input().split()))


H = [1]* 10
for l in List:
    H[l] = 0

I = [1]* 10
for i in List:
    I[i] = 0

cnt2 = 0
cnt3 = 0
RM(100,N)

if cnt2 == 0:
    cnt2 = 0x7FFFFFFF

if cnt3 == 0:
    cnt3 = 0x7FFFFFFF

print(min(result,cnt,cnt2,cnt3))





