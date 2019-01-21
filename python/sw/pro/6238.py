l=[]
for i in range(1, 101):
    if i%2 != 0:
        l += [str(i)]
print(', '.join(l))
