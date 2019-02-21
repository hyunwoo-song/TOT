import sys
sys.stdin = open('input.txt', 'r')

# 불필요하게 너무 많이 수행
# def Fibo(n):
#     if n <= 2:
#         return 1
#     else:
#         return(Fibo(n-1)+Fibo(n-2))
#
# print(Fibo(5))

# def Fibo2(n):
#     global memo
#     if n >= 2 and len(memo) <= n:
#         memo.append(Fibo2(n-1)+Fibo2(n-2))
#     return memo[n]
# memo = [0, 1]
#
# print(Fibo2(5))