import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

Data = list(map(int, input().split()))

Counts = [0]*10
h= 0

for i in Data:
    Counts[i] += 1

triplet = 0
run = 0

for j in range(len(Counts)):
    if Counts[j] // 3:
        triplet += j//3
        Counts[j] -= (Counts[j]//3)*3

while h < 10:
    for k in range(len(Counts)-2):
        if Counts[k] and Counts[k+1] and Counts[k+2]:
            Counts[k] -= 1
            Counts[k+1] -= 1
            Counts[k+2] -= 1
            run += 1
    h += 1


if run + triplet == 2:
    print("Baby Gin")
else:
    print("Lose")




