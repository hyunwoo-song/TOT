import sys

sys.stdin = open('input.txt', 'r')

Arr=list(map(int, input().split()))

n = len(Arr)

for i in range(1<<n):
    bin = []
    for j in range(n):
        if i & (1<<j):
            bin.append(Arr[j])
    print(bin)
    cin = []
    if sum(bin) == 0:
        cin.append(bin)
        for c in cin:
            print(c)




