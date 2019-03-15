import sys
sys.stdin = open('input.txt', 'r')


Fibo = [-1] * 101
Fibo[0] = 0
Fibo[1] = 1
# DP
# for now in range(2,101):
#     Fibo[now] = Fibo[now-1] + Fibo[now-2]
#
# print(Fibo[now])



def GetSome(num):
    if Fibo[num]==-1:
        Fibo[num] = GetSome(num - 1) + GetSome(num - 2)
        return Fibo[num]
    else:
        return Fibo[num]
    # basecase

print(GetSome(100))