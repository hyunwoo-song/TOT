import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    Danjo= list(map(int, input().split()))


    print('#{} {}'.format(t, sum))