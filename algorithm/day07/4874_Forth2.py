import sys
sys.stdin = open('input.txt' , 'r')

T = int(input())
for t in range(1, T+1):
    Code = input().split()
    len_C = len(Code)
    stack1=[]
    top2 = -1
    count = 0
    for c in range(len_C-1):
        if Code[c].isdigit():
            count += 1

    if count == len_C - count:
        for c in range(len_C-1):
            if Code[c].isdigit():
                stack1.append(int(Code[c]))
                top2 += 1


            else:
                if len(stack1) >= 2:
                    if Code[c] == '+':
                        stack1.pop()
                        A = stack1[top2-1] + stack1[top2]
                        stack1.pop()
                        stack1.pop()
                        top2 -= 2
                        stack1.append(A)
                        top2 += 1
                    elif Code[c] == '-':
                        stack1.pop()
                        A = stack1[top2 - 1] - stack1[top2]
                        stack1.pop()
                        stack1.pop()
                        top2 -= 2
                        stack1.append(A)
                        top2 += 1
                    elif Code[c] == '*':
                        stack1.pop()
                        A = stack1[top2 - 1] * stack1[top2]
                        stack1.pop()
                        stack1.pop()
                        top2 -= 2
                        stack1.append(A)
                        top2 += 1
                    elif Code[c] == '/':
                        stack1.pop()
                        A = int(stack1[top2 - 1] / stack1[top2])
                        stack1.pop()
                        stack1.pop()
                        top2 -= 2
                        stack1.append(A)
                        top2 += 1
        if stack1 != []:
            result = stack1[0]
        else:
            result = 'error'
    else:
        result = 'error'

    print(f'#{t} {result}')

