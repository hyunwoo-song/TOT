a = []
for i in range(1, 201):
    if (i % 5) : 
        if not i % 7:
            a += [str(i)]
b= ','.join(a)
print(b)

