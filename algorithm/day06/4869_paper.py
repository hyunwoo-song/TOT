import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    stack =[0]*100
        
    sq_1=[20, 10]
    sq_2=[20,20]
    sq_N=[20]
    sq_N.append(int(input()))
