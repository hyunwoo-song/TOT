import sys
sys.stdin = open('input.txt', 'r')

T = 10
for t in range(1, T + 1):
    len_S = int(input())
    Sick = list(map(str, input()))
    stack_N = []
    stack_4 = []
    for s in range(len_S):
        if Sick[s].isdigit():
            stack_N.append(int(Sick[s]))
        else:
            if Sick[s] == ')':
                while stack_4[-1] != '(':
                    stack_N.append(stack_4.pop())
                if stack_4[-1] =='(':
                    stack_4.pop()
            else:
                if Sick[s] == '+':
                    if stack_4:
                        if stack_4[-1] != '(':
                            stack_N.append(stack_4.pop())
                            stack_N.append(stack_4.pop())
                            stack_4.append(Sick[s])

                        else:
                            stack_4.append(Sick[s])
                    else:
                        stack_4.append(Sick[s])

                elif Sick[s] == '*':
                    if stack_4:
                        if stack_4[-1] != '(':
                            if stack_4[-1] == '+':
                                stack_4.append(Sick[s])

                            else:
                                stack_N.append(stack_4.pop())
                                stack_4.append(Sick[s])
                        else:
                            stack_4.append(Sick[s])
                    else:
                        stack_4.append(Sick[s])
                else:
                    stack_4.append(Sick[s])
    while stack_4:
        stack_N.append(stack_4.pop())

    print(stack_N)





