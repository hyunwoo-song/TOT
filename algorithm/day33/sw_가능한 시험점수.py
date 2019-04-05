import sys
sys.stdin = open('test.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Lst = list(map(int, input().split()))
    Visited=[]