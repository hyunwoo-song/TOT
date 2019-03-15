import sys
sys.stdin = open('1373.txt', 'r')

# A= input()
# result = 0
# Result=[]
# M=''
# for a in range(len(A)):
#     result += int(A[len(A)-a-1])*2**a
#
#
# while result:
#     c= result % 8
#     result //= 8
#     Result.append(c)
#
# for i in range(len(Result)-1,-1,-1):
#     M += str(Result[i])
# print(M)


A= input()
s = 0
Result = [-1]*7
k = ''
if int(A) < 8:
    print(A)
else:
    for i in range(len(A)-1,-1,-3):
        result = int(A[i])*2**(len(A)-i-1)+int(A[i-1])*2**(len(A)-(i-1)-1)+int(A[i-2])*2**(len(A)-(i-2)-1)
        result >>= 3*s
        Result[s]=result
        s += 1
    print(Result)
    for num in Result:
        if num==-1:
            break
        else:
            print(num,end="")
