import sys
sys.stdin=open('2637.txt')

N = int(input())
M = int(input())
L= []
Boo =[0]*(N+1)
for m in range(M):
    X, Y, K = map(int, input().split())
    L.append([X,Y,K])
L=sorted(L)[::-1]
l = 0

C = [1]*(N+1)
for r in range(len(L)):
    C[L[r][0]]=0

while l < len(L):
    if L[l][0] == N:
        t = L.pop(l)
        Boo[t[1]] =t[2]
        l=-1
    l += 1

j = 0
while L:
    for i in range(len(Boo)-1,-1,-1):
        if Boo[i]:

            while j < len(L):
                if L[j][0] == i:
                    p = L.pop(j)
                    Boo[p[1]] += p[2]*Boo[i]
                    j = -1
                j += 1
            j = 0

for i in range(1,len(C)):
    if C[i]:
        print('{} {}' .format(i, Boo[i]))




