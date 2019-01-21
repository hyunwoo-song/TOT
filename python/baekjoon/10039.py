T=[]
sum_T = 0
for i in range(5):
    T += [int(input())]
    if T[i] < 40:
        T[i] = 40
    sum_T += T[i]
print(int(sum_T/len(T))) 