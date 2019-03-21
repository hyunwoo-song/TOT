import sys
sys.stdin = open('ex3.txt', 'r')


def DFS(now,list):
    global cnt
    if sum(Sum) == 0:
        Result.add(tuple(result))



    if now+1 > len(D):
        return

    visited[now]=1
    result.append(D[now])
    DFS(now+1, Sum.append(D[now]))
    visited[now] = 0
    result.pop()
    DFS(now+1, Sum.pop())


D = [-1,3,-9,6,7,-6,1,5,4,-2]
cnt = 0
visited=[0]*10
result =[]
Sum=[]
Result=set()
DFS(0, Sum)
print(Result)
print(len(Result))
