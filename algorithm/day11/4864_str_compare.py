import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
for n in range(1,N+1):
    Pi = [-1, 0]
    Pattern = list(input())
    T = list(input())
    i=0
    j = 1
    while j < len(Pattern)-1:
        if Pattern[i] != Pattern[j]:
            if Pattern[0] != Pattern[j]:
                Pi.append(0)
            else:
                Pi.append(1)


        else:
            Pi.append(Pi[j] + 1)
            i += 1

        j += 1


    result = 0
    k = 0
    start = 0

    while start+k < len(T):

        if Pattern[k] == T[start+k]:
            k += 1
            if k == len(Pi):
                result = 1
                break
        else:
            start += k - Pi[k]
            k= 0
    print('#%d %d'%(n, result))