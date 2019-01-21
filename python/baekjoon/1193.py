X = int(input())

num = 1
hint = 1
count = 1
while X > num:
    hint += 1 
    num = num + hint
    count += 1

d = num - X
if count % 2:
    print(f'{1+d}/{count-d}')

else:
    print(f'{count-d}/{1+d}')
    