import sys
sys.stdin = open('input.txt', 'r')
T = 10
for t in range(1, T+1):
    N = int(input())
    Tree=[0]*(N+1)
    for n in range(N):
        List = list(input().split())
        Tree[int(List[0])] = List[1]

    