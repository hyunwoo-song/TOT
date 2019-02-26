import sys
sys.stdin = open('input.txt', 'r')

T = 10

for t in range(1, T+1):
    N = int(input())
    Table = []
    count = 0


    for n in range(N):
        Table.append(list(map(int, input().split())))

    for dx in range(N):
        New_T2 = []
        for dy in range(N):
            if Table[dy][dx]:
                New_T2.append(Table[dy][dx])

        if len(New_T2) >= 2:
            for i in range(len(New_T2)-1):
                if New_T2[i]==1:
                    if New_T2[i+1]==2:
                        count += 1

    print(f'#{t} {count}')

# for i in range(10):
#     n=int(input())
#     grid=[list(map(int,input().split())) for j in range(n)]
#     count=0
#     for x in range(100):
#         sign='neutral'
#         for y in range(100):
#             if grid[y][x]==1:
#                 sign='red'
#             elif grid[y][x]==2 and sign=='red':
#                 sign='neutral'
#                 count+=1
#     print(f'#{i+1} {count}')