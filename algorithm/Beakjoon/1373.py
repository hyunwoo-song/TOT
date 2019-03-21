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


# A= input()
# t= 0
# cnt = 0
# result = ''
# for a in range(len(A)-1,-1,-1):
#     t += int(A[a])*(1<<(cnt))
#     cnt += 1
#     if cnt ==3:
#         cnt = 0
#
#         result += str(t)
#         t = 0
# if A == '0':
#     print(0)
# if t:
#     result += str(t)
# for i in range(len(result)-1,-1,-1):
#     print(result[i], end='')

a = int(input(), 2)
print(a)
print('{}' .format(str(oct(a))[2:]))