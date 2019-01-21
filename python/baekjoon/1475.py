N =  input()
D= {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:2, 7:1, 8:1}
F= {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:2, 7:1, 8:1}
result = 1
N = N.replace('9','6')
for i in D.keys():
    while F[i] - N.count(str(i)) < 0:
        for j in range(9):
            F[j] += D[j]
        result += 1
print(result)

    






