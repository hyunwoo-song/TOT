import sys
sys.stdin = open('input.txt', 'r')

def Overlab(str):
    top = -1
    count = 0
    len_S = len(str)
    for s in range(len_S):
        if stack[top] != String[s]:
            top += 1
            stack[top] = String[s]
        else:
            stack[top]=0
            top-=1
    for l in range(len(stack)):
        if stack[l]:
            count += 1
    return count


T = int(input())
for t in range(1,T+1):
    String =input()
    stack=[0]*1000

    print(f'#{t} {Overlab(String)}')



# 함수 안쓰고
# T = int(input())
# for t in range(1, T + 1):
#     String = input()
#     len_S = len(String)
#     stack = [0] * 1000
#     top = -1
#     count = 0
#     for s in range(len_S):
#         if stack[top] != String[s]:
#             top += 1
#             stack[top] = String[s]
#         else:
#             stack[top] = 0
#             top -= 1
#     for l in range(len(stack)):
#         if stack[l]:
#             count += 1
#     print(f'#{t} {count}')
#