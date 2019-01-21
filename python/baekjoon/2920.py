T=[]
T +=  map(int, input().split())
count = 0
for i in range(7):
    if T[i]-T[i+1] == 1:
        count += 1
    elif T[i]-T[i+1] == -1:
        count -= 1
if count == -7:
    print('ascending')
elif count == 7:
    print('descending')
else:
    print('mixed')
        
