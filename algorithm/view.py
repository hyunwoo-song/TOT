import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

Data = list(map(int, input().split()))


count = 0
for i in range(2, len(Data)-2):
    k = Data[i]
    j = 0
    while j != k:
        if (Data[i]-Data[i-2]) >2:
            if (Data[i]-Data[i-1]) >2:
                if (Data[i] - Data[i+1]) > 2:
                    if (Data[i] - Data[i+2]) > 2:
                        count += 1
                        Data[i] -= 1
                        j += 1
print(count)