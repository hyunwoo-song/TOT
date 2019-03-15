import sys
sys.stdin = open('9613.txt', 'r')
def MAX0(x,y):
    global result
    Q= x
    W= y

    while x:
        if x < y:
            x, y = y, x
        x = x%y

    Result.append(y)
    return



T = int(input())
for t in range(1,T+1):
    Result = []
    Data= list(map(int, input().split()))
    for i in range(1,Data[0]):
        for j in range(i+1, Data[0]+1):
            MAX0(Data[i],Data[j])
    print(sum(Result))