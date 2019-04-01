import sys
sys.stdin = open('5249.txt')


def Find_Set(num):
    if num == P[num]:
        return num
    else:
        return Find_Set(P[num])

def Uninon(x, y,z):
    global result
    if Find_Set(x) != Find_Set(y):
        P[Find_Set(x)] = Find_Set(y)
        result+=z

def Make_Set(v):
    P[v] = v

TC =int(input())

for tc in range(1,TC+1):
    V, E = map(int,input().split())
    L=[]
    P = [0] * (V+ 1)
    result = 0
    for e in range(E):
        n1, n2, w = map(int,input().split())
        L.append([n1,n2,w])
    L.sort(key=lambda x:x[2])

    for j in range(1,V + 1):
        Make_Set(j)

    for z in range(len(L)):
        Uninon(L[z][0], L[z][1],L[z][2])

    print('#{} {}'.format(tc, result))