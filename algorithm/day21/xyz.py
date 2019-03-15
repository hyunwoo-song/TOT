# count=0
# for x in range(1,34):
#     for y in range(x,99):
#         for z in range(y, 99):
#             if x+y+z == 100:
#                 count +=1
#
# print(count)


def XYZ(a, b, c):
    global count

    if a> b or b >c or a >33:
        return

    if not(a, b, c) in Visited:
        if a +b +c== N:
            count += 1

            return

    XYZ(a+1,b,c)
    XYZ(a,b+1,c)
    XYZ(a,b,c+1)
    return count


N= 3
Visited =[[[0]*(N+1) for i in range(100)] for j in range(N+1)]
print(Visited)
count = 0
print(XYZ(1,1,1))