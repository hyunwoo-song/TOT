import sys
sys.stdin = open('5203.txt')

def Per(num,C,M):

    if num == C:
        print(M)
    else:
        for j in range(1,C+1):
            if j not in M:
                M[num+1] = j
                Per(num+1, C, M)
                M[num+1] = 0

def BABY(list,team):
    C = len(list)
    M = [0]*C

    Per(0,C,M)








T = int(input())
for tc in range(1,T+1):
    M=3
    Card = list(map(int,input().split()))
    A=[]
    B=[]
    result =0
    for i in range(len(Card)):
        if i%2:
            B.append(Card[i])
        else:
            A.append(Card[i])

        if i > 3:
            if i %2:
                BABY(B,2)
                break

            else:
                BABY(A,1)
                break


    print(result)

