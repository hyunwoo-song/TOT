import sys
sys.stdin = open('input.txt', 'r')


def My_push(x):
    global top
    top += 1
    stack[top] =x

def My_pop():
    global top
    if top == -1:
        return 0
    x= stack[top]
    top -= 1
    return x
def findnext(here):
    for next in range(8):
        if MyMap[here][next] and not visited[next]
            return next

def DFS(here):
    global top
    print(here)
    visited[here]= True

    while here:
        next = findnext(here)
        if next:
            My_push(here)
        while next:
            here = next
            print(here)
            vistied[here] = True
            next = findnext(here)
            My_push(here)
        here = My_pop()

    for next in range(8):
        if MyMap[here][next] and not visited[next]:
            DFS(next)

MyMap = [[0]*8 for i in range(8)]
visited= [0]*8

Data= list(map(int, input().split()))
howmany = int(len(Data)/2)

for i in range(howmany):
    start=Data[i*2]
    stop= Data[i*2+1]
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1


DFS(1)