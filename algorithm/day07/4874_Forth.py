import sys
sys.stdin = open('input.txt' , 'r')

T = int(input())
for t in range(1, T+1):
    Code = input().split()
    len_C = len(Code)
    stack2=[]
    top2 = -1
    count = 0
    for c in range(len_C-1):
        if Code[c].isdigit():
            count += 1

    if count == len_C -count:
        for c in range(len_C-1):

            if Code[c].isdigit():
                stack2.append(int(Code[c]))
                top2 += 1

            else:
                if len(stack2) >= 2:
                    if Code[c] == '+':
                        B = stack2[top2-1] + stack2[top2]

                    elif Code[c] == '-':
                        B = stack2[top2 - 1] - stack2[top2]

                    elif Code[c] == '*':
                        B = stack2[top2 - 1] * stack2[top2]

                    elif Code[c] == '/':
                        B = int(stack2[top2 - 1] / stack2[top2])
                    top2 -= 2
                    stack2.pop()
                    stack2.pop()
                    stack2.append(B)
                    top2 += 1

        result = stack2[0]
    else:
        result = 'error'

    print(f'#{t} {result}')

