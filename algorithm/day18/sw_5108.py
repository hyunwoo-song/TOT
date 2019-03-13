import sys
sys.stdin = open ('5108.txt', 'r')

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

def Enqueue(item):
    global head
    newNode = Node(item)

    if head == None:
        head=newNode
    else:
        p = head
        while p.link:
            p = p.link
        p.link = newNode

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    Arr = list(map(int, input().split()))
    head = None
    for arr in Arr:
        Enqueue(arr)
    p = head

    for m in range(M):
        arr_i, arr_n = map(int,input().split())
        k = p.link
        b = Node(arr_n)
        while arr_i>1 :
            arr_i -= 1
            p = p.link
            k = k.link
        p.link = b
        b.link =k
        p = head

    while L > 0 :
        L -= 1
        p = p.link

    print('#{} {}'.format(t,p.data))

