import sys
sys.stdin = open('twoint.txt', 'r')




T= int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A= list(map(int, input().split()))
    B= list(map(int, input().split()))

    Result=[]
    if len(A) > len(B):
        while len(A) >= len(B):
            result = 0
            for i in range(len(B)):
                result += A[i]*B[i]
            Result.append(result)
            A.pop(0)

    else:
        while len(B) >= len(A):
            result = 0
            for i in range(len(A)):
                result += A[i]*B[i]
            Result.append(result)
            B.pop(0)
            
    print('#{} {}'.format(t,max(Result)))