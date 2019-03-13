Input = [9,1,3,6,7,0,4,9,5,5]
Result = []
while Input:
    t= Input.pop(0)
    Result.append(t)
    for i in range(len(Result)-1,0,-1):
        print(i)
        if Result[i-1] > Result[i]:
            Result[i-1], Result[i] = Result[i], Result[i-1]
    print(Result)

