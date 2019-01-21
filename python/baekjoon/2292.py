T = int(input())
start = 2
count = 2
result= 0
hint = 6
result = start + hint -1
while result < T:
    count += 1
    hint += 6
    result = result + hint
if T == 1:
    count = 1
print(count)