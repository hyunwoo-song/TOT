import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

Data = list(map(int, input().split()))

print(Data)

max = Data[0]
maxindex = -1

# min = 0x7FFFFFFF




for i in range(len(Data)):
    if max < Data[i]:
        max = Data[i]
        maxindex = i

print(max)
print(maxindex+1)