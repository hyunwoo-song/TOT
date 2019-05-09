import sys
sys.stdin = open('treeMoney.txt')

import collections
def ISSAFE(y,x):
    if 0<=y<N and 0<=x<N:
        return True

def SPRING():
    for y in range(N):
        for x in range(N):
            if Tree[y][x]:
                alive=[]
                Tree[y][x].sort()
                while Tree[y][x]:
                    tree = Tree[y][x].pop(0)
                    if tree <= Map[y][x]:
                        Map[y][x] -= tree
                        alive.append(tree+1)
                    else:
                        Dead.append((tree,y,x))

                Tree[y][x].extend(alive)

def SUMMER():
    while Dead:
        d = Dead.pop()
        z=d[0]
        y= d[1]
        x= d[2]
        Map[y][x] += z//2

def FALL():
    for y in range(N):
        for x in range(N):
            for z in range(len(Tree[y][x])):
                if Tree[y][x][z] % 5 == 0:
                    for dir in range(8):
                        Y = y+Dy[dir]
                        X = x+Dx[dir]
                        if ISSAFE(Y,X):
                            Tree[Y][X].append(1)
def WINTER():
    for y in range(N):
        for x in range(N):
            Map[y][x] += A[y][x]

Dy=[-1,-1,-1,0,0,1,1,1]
Dx=[-1,0,1,-1,1,-1,0,1]
N, M, K = map(int, input().split())
A = [list(map(int,input().split())) for n in range(N)]
Map = [[5]*N for n in range(N)]
Tree = [[[] for _ in range(N)] for _ in range(N)]
Dead = collections.deque()

for m in range(M):
    x, y, z = map (int, input().split())
    Tree[y-1][x-1].append(z)
for k in range(K):
    SPRING()
    SUMMER()
    FALL()
    WINTER()

result = 0
for y in range(N):
    for x in range(N):
        if Tree[y][x]:
            result += len(Tree[y][x])
print(result)