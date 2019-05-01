import sys
sys.stdin = open('cattle.txt')

N, M, D = map(int,input().split())
L = [list(map(int,input().split())) for n in range(N)]
L.append([0]*M)

print(L)