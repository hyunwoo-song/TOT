import sys
sys.stdin =open('input.txt', 'r')

def Recur(n):
    if n == 1:
        return 1
    return n + Recur(n-1)

print(Recur(2))