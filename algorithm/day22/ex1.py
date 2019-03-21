import sys
sys.stdin = open('input.txt', 'r')

N = input()
t= 0
for n in range(len(N)):
    t = t*2 + int(N[n])
    if (n+1) % 7 == 0:
        print(t)
        t = 0

if (n+1)%7 !=0:
    print(t)