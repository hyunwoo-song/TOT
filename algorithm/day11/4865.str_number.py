import sys
sys.stdin = open('input.txt', 'r')

T= int(input())
for t in range(1, T+1):
    str1 = list(input())
    str2= list(input())
    str1 = list(set(str1))
    Count = [0]*(len(str1))

    for i in range(len(str1)):
        for s2 in str2:
            if str1[i] == s2:
                Count[i] += 1
    print('#%d %d' % (t, max(Count)))
