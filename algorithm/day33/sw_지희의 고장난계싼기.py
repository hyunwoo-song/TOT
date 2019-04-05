import sys
sys.stdin = open('broken.txt')


def CC(target, cnt):
    global result, finish, Result

    if result > Result:
        return

    if target == 1:
        if result == -1:
            Result = cnt + 1
            return

    flag = 0
    for t in str(target):
        if Cal[int(t)]:
            flag = 1
        else:
            flag = 0
            break
    if flag:
        result += len(str(target)) + cnt + 1
        finish = 1
        if Result > result:
            Result = result
        result -= len(str(target)) + cnt + 1

        return

    i = 2
    while i ** 2 <= target:
        if not target % i:
            H = target // i

            flag = 0
            for j in str(i):
                if Cal[int(j)]:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag:
                result += len(str(i))
                CC(H, cnt + 1)
                result -= len(str(i))
        i += 1


TC = int(input())
for tc in range(1, TC + 1):
    Cal = list(map(int, input().split()))
    G = int(input())
    result = -1
    Result = 0x7FFFFFFF
    finish = 0
    CC(G, 1)
    if Result == 0x7FFFFFFF:
        Result = -1
    print('#{} {}'.format(tc, Result))
