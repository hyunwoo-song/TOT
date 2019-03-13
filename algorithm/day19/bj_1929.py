import sys
sys.stdin = open('bj_1929', 'r')


def prime3(n): #O(Root n)
   if n<2:
       return
   i = 2
   while i*i<=n :
          if n%i ==0 :
              return
          i+=1
   return print(n)

M, N = map(int, input().split())

for i in range(M, N+1):
    prime3(i)
