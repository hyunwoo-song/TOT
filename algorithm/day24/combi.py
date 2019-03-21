A = [1,2,3,4,5]
R = []
for i in range(len(A)):
    for j in range(len(A)):
        if j >i:
            for k in range(len(A)):
                if k > i and k > j:
                    R.append([A[i],A[j],A[k]])


print(R)
print(len(R))

A = [1,2,3,4,5]
R = []
for i in range(len(A)):
    for j in range(len(A)):
        if j >= i:
            for k in range(len(A)):
                if k >= i and k >= j:
                    R.append([A[i],A[j],A[k]])

print(R)
print(len(R))

A = [1,2,3,4,5]
R = []
for i in range(len(A)):
    for j in range(len(A)):
        if j != i:
            for k in range(len(A)):
                if k != i and k != j:
                    R.append([A[i],A[j],A[k]])

print(R)
print(len(R))

A = [1,2,3,4,5]
R = []
for i in range(len(A)):
    for j in range(len(A)):
            for k in range(len(A)):
                R.append([A[i],A[j],A[k]])

print(R)
print(len(R))





