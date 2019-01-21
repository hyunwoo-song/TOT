# 퀵정렬로 죠지자
 
def quicksort(l):
    if len(l) <= 1:
        return l

    pivot = l[0]
    less= []
    more= []
    equal= []
    for i in l:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            equal.append(i)
    return quicksort(less) + equal + quicksort(more)

N = int(input())
a=[]
for _ in range(N):
    a.append(int(input()))
a_q=quicksort(a)
for i in a_q:
    print(i)

# N = int(input())
# a=[]
# for _ in range(N):
#     a.append(int(input()))
# b= sorted(a)
# for i in b:
#     print(i)