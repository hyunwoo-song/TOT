import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

Data = list(map(int, input().split()))


for j in range(len(Data)-1):
    for i in range(len(Data)-1-j):
        if Data[i] > Data[i+1]:
            Data[i], Data[i+1] = Data[i+1], Data[i]
print(Data)