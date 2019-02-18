import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용
N = int(input())
S_1= [0]*N
S_2= [0]*N

count = 0
pick = 0
select = 0
life = N
list = []

for n in range(N):
    S_1[n] += n+1
    S_2[n] = int(input())

for i in range(N):
    pick = S_1[i]
    select= S_2[i]
    for j in range(N):
        if pick != select:
            select[S_2[S_2[i]-1]]
        else:
            list.append()

