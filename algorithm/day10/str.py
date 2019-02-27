import sys
sys.stdin = open('input.txt', 'r')


Data = list(input())
l=[]
for i in range(len(Data)-1,-1, -1):
    l.append(Data[i])
print(l)