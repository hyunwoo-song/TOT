import sys
sys.stdin = open('input.txt', 'r')

stack= [0]*10 #시험시 10000
top = -1

# append 사용 O
# for i in range(1,4):
#     stack.append(i)
#
# while stack:
#     print(stack.pop())



# # append 사용 X
for i in range(1,4):
    top += 1
    stack[top] = i

# for i in range(3):
#     print(stack[top])
#     top -= 1

while top != -1:
    print(stack[top])
    top -= 1