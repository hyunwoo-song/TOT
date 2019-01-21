T = int(input())

for i in range(T):
    result= []
    R,S = input().split()
    for n in S:
        result += [n* int(R)]
        r = ''.join(result)
    print(r)
    
