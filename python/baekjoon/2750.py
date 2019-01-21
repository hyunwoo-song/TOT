N = int(input())
a=[]
b= []
for _ in range(N):
    a += [int(input())]
b= sorted(a)
for i in b:
    print(i)