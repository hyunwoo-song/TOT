import sys
sys.stdin = open('1463.txt', 'r')

def DP(Arr):
    Arr[1]= 0
    Arr[2]= 1
    Arr[3]= 1
    for i in range(4,len(Arr)):
        a = i-1
        b = Arr[i//2]+1
        c = Arr[i//3]+1


        Arr[i]=min(a,b,c)
        print(i, a, b, c)




N = int(input())
Arr=[0]*(N+1)
DP(Arr)


print(Arr)
