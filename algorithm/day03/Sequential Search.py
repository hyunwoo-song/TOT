import sys

sys.stdin = open('input.txt', 'r')

Arr=list(map(int, input().split()))
l= len(Arr)
N= 11


# for i in range(l):
#     if N == Arr[i]:
#         print('검색성공')
#         break


i = 0
while i < l and Arr[i] != N:
    i += 1
if i < l:
    print('검색성공')
else:
    print('실패')