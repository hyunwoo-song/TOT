import sys
sys.stdin = open('input.txt', 'r')


def RCP(index_a, index_b):
    global result, Winner
    if Tor[index_a-1] == 1:
        if Tor[index_b-1] == 2:
            Winner.append(index_b, Tor[index_b - 1])
        else:
            Winner.append(index_a, Tor[index_a - 1])

    elif Tor[index_a-1] == 2:
        if Tor[index_b-1] == 3:
            Winner.append(index_b, Tor[index_b - 1])
        else:
            Winner.append(index_a, Tor[index_a - 1])

    elif Tor[index_a-1] == 3:
        if Tor[index_b-1] == 1:
            Winner.append(index_b, Tor[index_b - 1])
        else:
            Winner.append(index_a, Tor[index_a - 1])

    return Winner

def Group(l):
    global N
    if N % 2:
        for _ in range(1,((N+1)//2)+1,2):
            RCP(l[_], l[_+1])

        for __ in range((N+1)//2, N,2):
            RCP(l[__], l[__+1])

    else:
        for _ in range(1, (N//2)+1, 2):
            RCP(l[_], l[_+1])
        for __ in range((N//2), N+1, 2):
            RCP(l[__], l[__+1])

T = int(input())
for t in range(1, T+1):
    result = 0
    N = int(input())
    Tor =list(map(int, input().split()))
    l = []
    Winner=[]
    for n in range(N):
        l.append([n+1, Tor[n]])
    print(l)
    print(Group(l))

