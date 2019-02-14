import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

Data = list(map(int, input().split()))

Counts = [0]*5

for i in Data:
    Counts[i] += 1


for j in range(1,len(Counts)):
    Counts[j] += Counts[j-1]

Temp = [0]* Counts[-1]

for k in Data:
    Temp[Counts[k]-1] = k
    Counts[k] -= 1
print(Temp)