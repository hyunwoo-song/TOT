N = int(input())
for n in range(1, N + 1):
    Pattern = list(input())
    T = list(input())
    i = 0
    k = 0
    result = 0
    while i < len(T):
        if T[i] == Pattern[k]:
            i += 1
            k += 1
            if k == len(Pattern):
                result = 1
                break

        else:
            i = i - k + 1
            k = 0

    print('#%d %d' % (n, result))