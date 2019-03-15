import sys
sys.stdin = open('2609.txt', 'r')

# A, B = map(int, input().split())
# Min0 = 1
# Max0 = 1
# C= 2
#
# if A > B:
#     A, B = B, A
#
# while B != C:
#     if not A % C and not B % C:
#         A //= C
#         B //= C
#         Max0 *= C
#     C += 1
# Min0 = Max0*A*B
#
# print(Max0)
# print(Min0)

A, B = map(int, input().split())
x= A
y= B
while x:
    if x < y:
        x, y = y, x
    x = x % y

result =y* A//y * B//y
print(y)
print(result)