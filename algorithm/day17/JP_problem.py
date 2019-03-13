class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

def Enqueue(item):
    global head,count
    newNode = Node(item)

    if head == None:
        head=newNode
    else:
        p = head
        while p.link and p.link!= head:
            p = p.link
        p.link = newNode
        count += 1
        p = p.link
        p.link = head




head = None
count=0

for i in range(1,10):
    Enqueue(i)

p = head
while p.link.link != p:
    p.link.link = p.link.link.link


print(p.data)
print(p.link.data)