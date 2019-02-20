import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

def find_1(list):
    index = 0
    for i in range(1, len_s, 2):
        min = stick[1]
        if stick[i] < min:
            min = stick[i]
            index = i
    bin.append(stick[index-1])
    bin.append(stick[index])
    return bin

T = int(input())
for t in range(1, T+1):
    N = int(input())
    stick = list(map(int, input().split()))
    len_s =len(stick)
    bin=[]
    bin = find_1(stick)
    count = N-1
    while count > 0 :
        index = 0
        for j in range(0, len_s, 2):
            if bin[-1] == stick[j]:
                index = j
        bin.append(stick[index])
        bin.append(stick[index+1])
        count -=1



    print(f'#{t} {" ".join(map(str, bin))}')


