import sys
sys.stdin = open('input.txt', 'r')


def RCP(Start, End):

    if (l[Start][1] -l[End][1]) == 1:
        Winner.append(l[Start])
    elif (l[Start][1] -l[End][1]) == -1:
        Winner.append(l[End])
    elif l[Start][1] == 1:
        Winner.append(l[Start])
    else:
        Winner.append(l[End])
    return print(Winner)


T = int(input())
for t in range(1, T+1):
    result = 0
    N = int(input())
    Tor =list(map(int, input().split()))
    l = [[0,0]]
    Winner=[]
    for n in range(N):
        l.append([n+1, Tor[n]])
    print(l)

    RCP(1,2)
