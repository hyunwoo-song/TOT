# def GetSome1(count):
#     if count == 0:
#         return
#     print('재귀%d' %count)
#     GetSome1(count-1)
#
# GetSome1(3)
#
# def GetSome2(count):
#     if count == 0:
#         return
#     GetSome2(count - 1)
#     print('재귀%d' %count)
#
#
# GetSome2(3)


def fibo(n):
    global memo
    if n >= 2 and len(memo) <= n :
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo= [0, 1]