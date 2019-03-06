import sys
sys.stdin = open('input.txt', 'r')




# def DFS(i):
#     global result
#
#     result += n_list[i]
#
#     if result <= 40:
#         Result.append(result)
#
#         for j in range(i + 1, n):
#             DFS(j)
#             result -= n_list[j]
#
#     else:
#         return

def DFS(now,sum):

    if sum > 40:
        return

    if now+1 > n:
        return Sum.append(sum)

    DFS(now+1, sum+n_list[now])
    DFS(now+1, sum)
    Sum.append(sum)


B = int(input())
n = int(input())
n_list = list(map(int, input().split()))
Sum=[]
DFS(0, 0)
print(Sum)
print(max(Sum))

