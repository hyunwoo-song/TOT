import sys
sys.stdin = open('treeMoney.txt')

import collections
Dead = collections.deque()

def ISSAFE(y,x):
    if 0<=y<N and 0<=x < N:
        return True

def SPRING():
    l = len(Que)
    while l>0:
        l -= 1
        t = Que.pop()
        z = t[0]
        y = t[1]
        x = t[2]
        if z > 0:
            if Map[y][x] >= z:
                Map[y][x] -= z
                Que.appendleft((z+1,y,x))

            else:
                Dead.append((z,y,x))

def SUMMER():
    while Dead:
        t = Dead.popleft()
        z= t[0]//2
        y=t[1]
        x=t[2]
        Map[y][x] += z

def FALL():
    for q in range(len(Que)-1,-1,-1):
        z = Que[q][0]
        y = Que[q][1]
        x = Que[q][2]
        if z % 5 == 0:
            for dir in range(8):
                Y = y+Dy[dir]
                X = x+Dx[dir]
                if ISSAFE(Y,X):
                    Que.append((1,Y,X))



def WINTER():
    for y in range(N):
        for x in range(N):
            Map[y][x] += Arr[y][x]

Dy=[-1,-1,-1,0,0,1,1,1]
Dx=[-1,0,1,-1,1,-1,0,1]

N, M, K = map(int, input().split())
Arr = [list(map(int, input().split())) for n in range(N)]
Que = collections.deque()
Map = [[5]*N for n in range(N)]
turn = K

for m in range(M):
    x,y,z = map(int,input().split())
    Que.append((z, y-1, x-1))

while turn > 0:
    SPRING()
    SUMMER()
    FALL()
    WINTER()
    turn -= 1

result = 0
for z in range(len(Que)):
    if Que[z][0]:
        result += 1
print(result)