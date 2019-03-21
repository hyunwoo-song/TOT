N = 123
result =''
while N // 7:
    result += str(N % 7)
    N //= 7
result += str(N)

for r in range(len(result)-1,-1,-1):
    print(result[r],end='')




# def Getsome(n,k):
#     if n < k:
#         print(n, end='')
#         return
#     else:
#         Getsome(n//k,k)
#         print(n%k,end='')
#
# Getsome(123,7)