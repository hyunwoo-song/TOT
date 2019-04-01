import sys
sys.stdin = open('2606.txt')

def Find_Set(num):
    if num == P[num]:
        return num
    else:
        return Find_Set(P[num])

def Make_Set(v):
    P[v] = v

def Uninon(x, y):
    P[Find_Set(x)] = Find_Set(y)

Com_N= int(input())
link_N= int(input())
P= [0]* (Com_N+1)
Rank = [0]* (Com_N+1)

for j in range(1, Com_N+1):
    Make_Set(j)

for n in range(link_N):
    m, s = map(int, input().split())
    Uninon(m, s)


cnt = 0
for i in range(1,Com_N+1):
    if Find_Set(1) == Find_Set(i):
        cnt +=1
print(cnt-1)
