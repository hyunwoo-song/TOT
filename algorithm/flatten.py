import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용


T = 10
for t in range(1, T+1):
    dump = int(input())
    heights = list(map(int, input().split()))


    result = 0x7FFFFFFF
    max_i = 0
    min_i = 0
    while dump > -1:
        max_h = 0
        min_h = 0x7FFFFFFF
        for i, h in enumerate (heights):
            if max_h < h:
                max_h = h
                max_i = i

            if min_h > h:
                min_h = h
                min_i = i
        result = max_h - min_h
        heights[max_i] -=1
        heights[min_i] += 1
        dump -= 1


    print(f'#{t} {result}')



    # for n in range(dump):
    #     max_h = max(heights)
    #     min_h = min(heights)
    #     for i in range(len(heights)):
    #         if max_h == heights[i]:
    #             heights[i] -=1
    #         if min_h == heights[i]:
    #             heights[i] += 1
    #             break
    #         result = max_h - min_h
    #     if result == 0 or result == 1:
    #         break
    #

