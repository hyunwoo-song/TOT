import sys
sys.stdin = open('2jin.txt')

def BN(num,start,end):
    global count, flag


    mid = (start+end)//2
    if mid < start:
        return
    if mid > end:
        return

    if S_N[mid] == num:
        count += 1
        flag=0
        return

    elif S_N[mid] > num:
        if flag == 0 or flag == 2:
            flag = 1
        else:
            flag = 0
            return
        BN(num, start, mid-1)


    elif S_N[mid] < num:
        if flag == 0 or flag == 1:
            flag = 2
        else:
            flag = 0
            return
        BN(num, mid +1, end)


    # else:
    #     return




TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    List_N = list(map(int, input().split()))
    List_M = list(map(int, input().split()))
    S_N = sorted(List_N)
    count = 0
    flag = 0

    for m in range(len(List_M)):
        BN(List_M[m],0, N-1)
    print(count)
