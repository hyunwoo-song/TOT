front = -1
rear = -1


def BFS(here):
    global front, rear
    rear += 1
    Queue[rear] = here
    visited[here] = True

    while front != rear:
        front += 1
        here = Queue[front]
        print(here)
        for next in range(N+1):
            if Mymap[here][next] and not visited[next]:
                visited[next]=True
                Distance[next] = Distance[here]+1
                Parent[next] = here
                rear += 1
                Queue[rear] = next


N = 7
Queue=[0]*(N+1)
Parent = [-1] * (N + 1)
Distance = [0x7FFFFFFF] * (N + 1)
visited = [0] * (N + 1)
result = 0
L = list(map(int, (input().split())))
Mymap = [[0] * (N + 1) for _ in range(N + 1)]
for l in range(0, len(L), 2):
    Mymap[L[l]][L[l + 1]] = True

BFS(1)