def Sel(list):
    if not list:
        return

    min_l = 0x7FFFFFFF
    min_i = 0
    for i in range(len(list)):
        if list[i]< min_l:
            min_l = list[i]
            min_i = i
    R.append(list.pop(min_i))
    Sel(list)




 
L = [8, 4 ,3 ,11 ,2, 50]
R = []
Sel(L)
print(R)


