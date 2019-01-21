# import sys
# T = int(sys.stdin.readline())
# for n in range(T):
#     x, y = map(int, sys.stdin.readline().split())
#     D = (y-x)
#     count = 0
#     go = 1
#     while D != 0:
#         if (go+sum(range(0,go))) <= D:
#             D = D - go 
#             go += 1
#             count += 1
            
#         else:
#             go -= 1
    
#     print(count)

# def warp(D):
#     count = 0
#     go = 1
#     while D != 0:
#         sum_go = sum(range(go))
#         if (go+sum_go) <= D:
#             D = D - go 
#             count += 1
#             go += 1
            
#         else:
#             go -= 1
            
#     return count

# import sys
# T = int(sys.stdin.readline())
# for n in range(T):
#     x, y = map(int, sys.stdin.readline().split())
#     dist = y - x
#     print(warp(dist))


for n in range(int(input())):
    x, y = map(int, input().split())
    D =(y-x)
    count =0
    n = 1
    while(1):
        if n**2<= D and D< (n+1)**2:
            count += (2*n-1) 
            if D == n**2:
                count = count
            elif D <= n**2+ n: 
                count += 1 
            else:
                count += 2
            break
        else:
            n += 1
    print(count)

