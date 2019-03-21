import sys
sys.stdin = open('babyjin.txt', 'r')


def BABY(a,b,c):
    if a == b == c:
        return True
    elif int(a) == int(b)-1 and int(b) == int(c)-1:
        return True
    elif int(c) == int(b)-1 and int(b) == int(a)-1:
        return True
    else:
        return False
T = 4
for t in range(4):
    N = list(map(int,input().split()))
    Visited= [[[[[[0]* 10 for _ in range(10)] for __ in range(10)] for ___ in range(10)] for ____ in range(10)] for _____ in range(10)]
    for n1 in range(len(N)):
        for n2 in range(len(N)):
            if n2 != n1:
                for n3 in range(len(N)):
                    if n3 != n2 and n3 != n1:
                        for n4 in range(len(N)):
                            if n4 != n3 and n4 != n2 and n4 != n1:
                                for n5 in range(len(N)):
                                    if n5 != n4 and n5 != n3 and n5 != n2 and n5 != n1:
                                        for n6 in range(len(N)):
                                            if n6 != n5 and n6 != n4 and n6 != n3 and n6 != n2 and n6 != n1:
                                                if BABY(N[n1],N[n2],N[n3]) and BABY(N[n4],N[n5],N[n6]):
                                                    if not Visited[N[n1]][N[n2]][N[n3]][N[n4]][N[n5]][N[n6]]:
                                                        Visited[N[n1]][N[n2]][N[n3]][N[n4]][N[n5]][N[n6]] = True
                                                        print('{}{}{}{}{}{}'.format(N[n1],N[n2],N[n3],N[n4],N[n5],N[n6]))
    print(N)
    print('kkkkkkkkkkkkkkkkkkkkkkkkkkk')

######
def COM(a, b):
    D = [i for i in range(1, a+1)]
    for d in range(len(D)):
        D[d]

COM(5,3)
