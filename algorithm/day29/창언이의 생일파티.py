import sys
sys.stdin = open('party.txt')



TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    A=[]
    L=[]
    C=[]
    for m in range(M):
        a, b = map(int,input().split())
        L.append([a,b])
        if a == 1:
            A.append(b)
        if b==1:
            A.append(a)


    for l in range(len(L)):
        for r in A:
            if r in L[l]:
                for ll in L[l]:
                    if r != ll and ll != 1:
                        C.append(ll)

    print('#{} {}' .format(tc, len(set(C))))
