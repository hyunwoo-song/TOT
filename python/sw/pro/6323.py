#피보나티

N= int(input())
l = [1, 1]
for i in range(1, N-1):
    l.append(l[i-1]+l[i])
print(l)