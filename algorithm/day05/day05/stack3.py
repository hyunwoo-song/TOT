import sys
sys.stdin = open('input.txt', 'r')

stack = [0]* 10
top = -1
Info = [-1]*128 # char 1bytr ASCII code 7bit
Data =input()

Info[ord(')')]='('
Info[ord(']')]='['
Info[ord('}')]='{'
Info[ord('>')]='<'

count =0
howmany= len(Data)
for i in range(howmany):
    if (Data[i]=='(' or Data[i]=='{' or Data[i]=='[' or Data[i]=='<'):
        top += 1
        stack[top] = Data[i]

    elif stack[top] == Info[ord(Data[i])]:
        stack.pop()
        top -= 1

    elif not stack[top]:
        if (Data[i]==')' or Data[i]=='}' or Data[i]==']' or Data[i]=='>'):
            count = 1
            break

if top != -1 or count== 1:
    print('f')

else:
    print('진민재')


