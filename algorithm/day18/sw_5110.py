import sys
sys.stdin = open ('5110.txt', 'r')


class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


def Enqueue(item):
    global head, end
    newNode = Node(item)

    if head == None:
        head = newNode
    else:
        p = head
        while p.link:
            p = p.link

        p.link = newNode
        end = p.link

    return


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    p = None
    z = None
    q = None
    for m in range(M):
        head = None
        end = None
        Arr = list(map(int, input().split()))
        for arr in Arr:
            Enqueue(arr)
        while q:
            if z.data > head.data:
                end.link = q
                break
            if q.data >= head.data:
                if q.link:
                    k = q.link
                q.link = head
                end.link = k
                break
            q = q.link
            if not q.link:
                q.link = head
                break

        if not z:
            z = head
        q = z
    u = 0
    Result = []
    Result2 = []
    Result3=[]
    while u < 10:
        u += 1
        y = z
        while y.link:
            j = y
            y = y.link
            Result.append([j.data,y.data])
    for h in range(10):
        Result2.append(Result.pop(-1))
        b= Result2.pop(0)
        Result3.append(b[1])
    Result3 =' '.join(map(str, Result3))
    print('#{} {}'.format(t,Result3))

