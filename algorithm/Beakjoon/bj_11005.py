import sys
sys.stdin = open('11005.txt', 'r')

A, B = map(int, input().split())
C = []
R = ''
while A:
    C.append(A%B)
    A //=B

for c in range(len(C)-1,-1,-1):
    if C[c] >= 10:
        R += chr(C[c]+55)
    else:
        R += str(C[c])
print(R)

