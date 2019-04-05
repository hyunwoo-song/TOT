import sys
sys.stdin = open('input.txt')

def GO1(num):
    if Mymap[num][2]:
        A.append(Mymap[num][2])
        GO1(Mymap[num][2])

    else:
        return
def GO2(num):
    if Mymap[num][2]:
        B.append(Mymap[num][2])
        GO2(Mymap[num][2])

    else:
        return
def C(num):
    global cnt

    if Mymap[num][0]:
        cnt += 1
        C(Mymap[num][0])
    if Mymap[num][1]:
        cnt += 1
        C(Mymap[num][1])
    else:
        return

TC = int(input())
for tc in range(1,TC+1):
    V, E, Find_A, Find_B = map(int, input().split())
    Lst = list(map(int, input().split()))
    Mymap = [[0]*3 for v in range(V+1)]


    for l in range(0,len(Lst),2):
        if not Mymap[Lst[l]][0]:
            Mymap[Lst[l]][0] = Lst[l+1]
            Mymap[Lst[l + 1]][2] = Lst[l]

        else:
            Mymap[Lst[l]][1] = Lst[l + 1]
            Mymap[Lst[l + 1]][2]= Lst[l]

    A = []
    B = []
    GO1(Find_A)
    GO2(Find_B)
    flag = 0
    for b in B:
        for a in A:
            if b == a:
                result = a
                flag = 1
                break
        if flag:
            break
    cnt = 0
    C(result)
    print('#{} {} {}'.format(tc, result, cnt+1))