import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용
def find_1(list):
    index = 0
    bin=[]
    for i in range(0, len_s, 2):
        count = 0
        for j in range(1, len_s, 2):
            if stick[i] == stick[j]:
                count += 1
                break
        if count == 0:
            index = i
    bin.append(stick[index])
    bin.append(stick[index+1])
    return bin


T = int(input())
for t in range(1, T+1):
    N = int(input())
    stick = list(map(int, input().split()))
    len_s =len(stick)
    bin=find_1(stick)
    life = N-1
    while life > 0:
        for i in range(0, len_s, 2):
            if bin[-1] == stick[i]:
                bin.append(stick[i])
                bin.append(stick[i+1])

        life -= 1
    print(f'#{t} {" ".join(map(str, bin))}')