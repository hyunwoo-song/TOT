import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

Data = list(map(int, input().split()))

cand1 = 0
cand2 = 0

for index_1 in range(len(Data)-1,0,-1):
    if Data[index_1] > Data[index_1-1]:
        cand1 = Data[index_1-1]
        break
for index_2 in range(index_1-1,len(Data)):
    if cand1 < Data[index_2]:
        cand2 = Data[index_2]
        if Data[index_2] < cand1:
            break
if cand1 == 0:
    print(Data)
else:
    Data[index_1-1], Data[index_2] = cand2, cand1
    Data[index_1:]=Data[:index_1-1:-1]
    print(Data)