T= int(input())
for i in range(T):
    user_input = input().split('X')
    result = 0
    for n in user_input:
        count=0
        d = 0 
        count += n.count('O')
        if count >0:
            for j in range(1, count+1):
                d += j
            result += d
    print(result)