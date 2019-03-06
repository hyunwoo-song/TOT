import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for t in range(1,T+1):
    N= int(input())
    Farm = [list(map(int,list(input()))) for _ in range(N)]
    sum = 0
    Farm2=[]
    for n in range(N):
        Farm2.append(list(map(int, list(input()))))
    print(Farm)
    print(Farm2)

    result=0