import sys
sys.stdin= open('input.txt', 'r')

IDT = [0]* (1<<5)
Data=list(map(int, input().split()))
howmany = len(Data)

def update(a,b): # 3, 1
    where = base + a -1
    IDT[where] = b
    where >>= 1

    while where:
        IDT[where] = IDT[where*2]+IDT[where*2+1]
        where >>= 1

def RSQ(ffrom, to): # 1, 4
    ffrom = ffrom +base -1 # 8
    to = to + base -1  # 11
    sum = 0
    print(ffrom, to)
    while ffrom < to :
        if ffrom%2:
            sum += IDT[ffrom]
            ffrom += 1
        if not to%2:
            sum += IDT[to]
            to -=1
        ffrom >>= 1
        to >>= 1

    if ffrom == to:
        sum += IDT[ffrom]
        print(sum)




base = 1
while base < howmany:
    base <<= 1


for now in range(base, howmany + base):
    IDT[now] = Data.pop(0)

for parent in range(base-1, 0, -1):
    IDT[parent] = IDT[parent*2]+IDT[parent*2+1]

print(IDT)
update(3,1)
print(base)
RSQ(1,2)

