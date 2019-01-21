# import sys
# T= int(sys.stdin.readline())
# for _ in range(T):
#     M, N, x, y = map(int, sys.stdin.readline().split())

#     d= abs(M-N)
#     i= [M,N]
#     b = [x,x,y]
#     if M > N:
#         i = [N,M]
#         b = [y,y,x]
    
#     b[1] = b[1]-d
#     if b[1] <0 :
#         b[1]=i[1]-b[1]
#     count =b[0]+i[0]

#     while b[1] != b[2]:
#         b[1] = b[1]-d
#         if b[1] <0 :
#             b[1]=i[1]+b[1]
#         count = count + i[0] 
#         if count > M*N:
#             count = -1
#             break

#     print(count)



T= int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    i = 0
    count = 0 
    y1 = 0
    while y != y1:
        i += 1
        y1 = (M*i + x) % N
        count = (M*i + x)
        if y1 == 0:
            y1 == N
        if count > M*N:
            count = -1
            break
    print(count)
