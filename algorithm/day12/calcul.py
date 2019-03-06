import sys
sys.stdin = open('input.txt', 'r')

T =10
for t in range(1, T+1):
    N= int(input())
    Map = list(input())
    Stack=[]
    Stack_4= []
    for m in Map:
        if m.isdigit():
            Stack.append(m)
        else:
            Stack_4.append(m)