import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    code = input()
    result = -1
    stack = [0]*100
    top = -1
    l_code = len(code)

    Info = [-1] * 128
    Info[ord(')')] = '('
    Info[ord('}')] = '{'

    count= 0

    for c in range(l_code):
        if code[c] == '{'  or code[c]=='(':
            top += 1
            stack[top] = code[c]

        elif stack[top] == Info[ord(code[c])]: #
            stack.pop()
            top -= 1

        elif not stack[top]:
            if code[c] == ')' or code[c] == '}':
                count = 1
                break

        elif code[c] == ')' or code[c] == '}':
            if stack[top] != Info[ord(code[c])]:
                count = 1
                break


    if top != -1 or count == 1:
        result = 0

    else:
        result = 1
    print(f'#{t} {result}')
