import sys
sys.stdin = open('input.txt', 'r')

def DFS(now,list):
    global N,C
    if len(Sum) == C:
        for i in range(10):
            if visited[i]:
                result.append(i)
        return

    if now+1 > N:
        return

    visited[now+1]=1
    DFS(now+1, Sum.append(n_list[now]))
    visited[now+1] = 0
    DFS(now+1, Sum.pop())


N= int(input())
C= int(input())
n_list = [i for i in range(1, N+1)]
Sum=[]
result=[]
visited = [0] * 10
DFS(0, Sum)

print(result)