import sys
sys.stdin = open('input.txt', 'r')

stack = [0]* 10


for _ in range(2):
    top = -1
    Data = input()
    for d in range(len(Data)):
        if Data[d] == '(':
            top += 1
            stack[top] = Data[d]

        elif Data[d] == ')':
            stack[top]= 0
            top -=1


    # if stack[top]:
    #     print('f')
    # else:
    #     print('진민재')


    if top != -1:
        print('f')
    else:
        print('진민재')




