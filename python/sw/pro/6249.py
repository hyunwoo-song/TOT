T= input()
D = {'0':0, '1':0, '2':0, '3':0, '4':0, 
    '5':0, '6':0, '7':0, '8':0, '9':0}
i = -1 
l_1 =[]
l_2 = []
for k in D.keys():
    D[k] = T.count(k)
    i += 1
    l_1 += [str(i)]
print(' '.join(l_1))

for v in D.values():
    l_2 += [str(v)]
print(' '.join(l_2)) 