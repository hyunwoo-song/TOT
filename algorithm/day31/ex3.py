import sys
sys.stdin = open('ex3')


import itertools

TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    Cookie = list(map(int,input().split()))
    Robot = list(map(int,input().split()))
    result = 0
    Result = 0x7FFFFFFF
    C = [n for n in range(N)]
    L = list(map(list, (itertools.permutations(list(C), N))))
    for l in range(len(L)):
        i = 0
        for ll in L[l]:
            result += abs(abs(Cookie[2*ll])-abs(Robot[2*i]))+abs(abs(Cookie[2*ll+1])-abs(Robot[2*i+1]))
            i += 1
        if Result > result:
            Result = result
        result = 0

    print('#{} {}'.format(tc, Result))