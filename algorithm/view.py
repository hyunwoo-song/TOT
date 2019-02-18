import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

## 나의 코딩






T = 10
for t in range(1,T+1):
    N = int(input())
    heights = list(map(int, input().split()))
    result = 0

    for i in range(2, len(Data) - 2):
        if Data[i] > Data[i + 2] and Data[i] > Data[i - 2]:
            if Data[i] > Data[i + 1] and Data[i] > Data[i - 1]:
                result = Data[i] - max(Data[i - 2], Data[i - 1], Data[i + 1], Data[i + 2])
                count += result

    print(f'#{t} {result}')



# def getMax(here):
#     mymax = heights[here-2]
#     if mymax < heights[here-1]:
#         mymax = heights[here-1]
#     if mymax < heights[here+1]:
#         mymax = heights[here+1]
#     if mymax < heights[here+2]:
#         mymax = heights[here+2]
#
#     return mymax
#
#
#
# T = 10
# for t in range(1,T+1):
#     N = int(input())
#     heights = list(map(int, input().split()))
#
#     result = 0
#
#     for here in range(2, N-2):
#         side = getMax(here)
#         if side < heights[here]:
#             result += heights[here] - side
#
#
#
#     print(f'#{t} {result}')