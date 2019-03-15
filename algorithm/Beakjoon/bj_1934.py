import sys
sys.stdin = open('1934.txt', 'r')

def MIN0(x,y):
    Q= x
    W= y

    while x:
        if x < y:
            x, y = y, x
        x = x%y

    result = (Q//y)*W
    return result




T = int(input())
for t in range(1,T+1):
    A, B = map(int, input().split())
    print(MIN0(A,B))