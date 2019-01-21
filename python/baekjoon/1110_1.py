N = int(input())
count = 1
fff=N
result = 0
a = N // 10
b = N % 10
inputsum = (a+b)%10
newnum=b*10+inputsum
while newnum != N:
    a = newnum // 10
    b = newnum % 10
    inputsum=(a+b)%10
    newnum=b*10+inputsum
    count += 1
    if newnum == N:
        break
print(count)