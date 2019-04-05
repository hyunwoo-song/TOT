import sys
sys.stdin = open('1107.txt')

from collections import deque

def RM2(start, end):
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
        cnt2 += abs(int(U) - int(end))


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
        cnt3 += abs(int(T) - int(end))


Que = deque()

def VISIT(string,end):
    c = len(string)
    if string == '0':
        string = ''
        if K[int(end[c-1])]:
            string += str(end[c])
            Que.append(string)

        else:
            s1 = ''
            s2 = ''
            for k1 in range(int(end[c]), -1, -1):
                if K[k1]:
                    temp = s1 + str(k1)
                    if not temp in Que:
                        Que.append(temp)
                    break

            for k2 in range(int(end[c])+1, 10):
                if K[k2]:
                    temp = s2 + str(k2)
                    if not temp in Que:
                        Que.append(temp)
                    break

    else:
        if K[int(end[c])]:
            temp = string + str(end[c])
            if not temp in Que:
                Que.append(temp)
        else:
            s1=string
            s2=string
            for k1 in range(int(end[c]),-1,-1):
                if K[k1]:
                    temp = s1+str(k1)
                    if not temp in Que:
                        Que.append(temp)
                    break

            for k2 in range(int(end[c])+1,10):
                if K[k2]:
                    temp = s2 + str(k2)
                    if not temp in Que:
                        Que.append(temp)
                    break




def RM(start, end):

    Que.append(str(0))

    while Que:
        t = Que.popleft()
        if len(t) < len(end):
            VISIT(t,end)
        elif len(t) == len(end):
            cnt = abs(int(end)-int(t)) + len(t)
            Result.append(cnt)







N = input()
M = int(input())
List = list(map(int, input().split()))
K = [1] * 10
for l in List:
    K[l] = 0
Result=[0x7FFFFFFF]
result = abs(int(N)-100)

RM(100, N)

H = [1]* 10
for l in List:
    H[l] = 0

I = [1]* 10
for i in List:
    I[i] = 0

cnt2 = 0
cnt3 = 0
RM2(100,N)

if cnt2 == 0:
    cnt2 = 0x7FFFFFFF

if cnt3 == 0:
    cnt3 = 0x7FFFFFFF

print(min(min(Result),result,cnt2,cnt3))


