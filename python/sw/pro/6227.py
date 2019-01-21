l = []
for i in range(100,301):
    if not (i // 100) % 2:
        if not ((i % 100) //10) % 2:
            if not ((i % 100) % 10) % 2:
                l += [str(i)]
b = ','.join(l)
print(b)