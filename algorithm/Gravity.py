import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

Data = list(map(int, input().split()))

max = Data[0]
maxindex = 0
count = 0

for i in range(len(Data)):
    if max < Data[i]:
        max = Data[i]
        maxindex = i

for j in Data:
    if max != j:
        count += 1
print(len(Data) - count)







