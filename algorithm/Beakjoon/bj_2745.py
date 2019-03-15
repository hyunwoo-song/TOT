import sys
sys.stdin = open('2745.txt', 'r')

N, B = map(str, input().split())
C=[0]*len(N)
result = 0
for i in range(len(N)):
    if ord(N[i])<= 90 and 65 <= ord(N[i]):
        C[i] = ord(N[i]) - 55
    else:
        C[i] = int(N[i])

for c in range(len(C)):
    result += C[len(C)-1-c]*int(B)**c
print(result)
