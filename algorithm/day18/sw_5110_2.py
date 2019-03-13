import sys
sys.stdin = open ('5110.txt', 'r')

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def Enqueue(item):
    global head, end, z, a
    newNode = Node(item)

    if head == None:
        head = newNode

    else:
        p = head
        while p.right:
            p = p.right
        newNode.left = p
        p.right = newNode
        z = newNode
        end = p.right

    return


T = 1
for t in range(1, T + 1):
    N, M = 4, 4
    p = None
    a = None
    z = None
    q = None
    for m in range(M):
        head = None
        end = None
        Arr = list(map(int, input().split()))
        for arr in Arr:
            Enqueue(arr)
        while q:
            if a.data > head.data:
                end.right = q
                a.left = end
                a = head

                break
            if not q.right:
                q.right = head
                head.left = q
                break

            if q.data >= head.data:
                x = q.right
                head.left = x.left
                x.left = end
                end.right = x
                q.right = head

                break
            q = q.right



        if not a:
            a = head
        q = a

    while end.right:
        end = end.right
    Result = []
    for i in range(10):
        Result.append(end.data)
        end = end.left

    print(Result)