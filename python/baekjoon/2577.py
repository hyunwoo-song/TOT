A = int(input()); B = int(input()); C = int(input())
D = str(A * B * C)
E= []
count = 0

for n in D:
    E += map(int, n)

for i in (range(10)):
    count = E.count(i)
    print(count)