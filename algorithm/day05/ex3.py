import sys
sys.stdin = open('input.txt', 'r')

MyMap = [[0]*8 for i in range(8)]
visited= [0]*8

def DFS(here):
    print(here)
    visited[here]= True

    for next in range(8):
        if MyMap[here][next] and not visited[next]:
            DFS(next)


Data= list(map(int, input().split()))
howmany = int(len(Data)/2)

for i in range(howmany):
    start=Data[i*2]
    stop= Data[i*2+1]
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1


DFS(1)