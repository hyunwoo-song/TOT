import sys
sys.stdin = open('max.txt')

def SF(start, cnt, goal):
    global result
    A = []

    if result:
        return

    if cnt <= 0:
        result = start
        return

    if start == goal:
        if cnt % 2:
            for i in range(len(start)):
                if start.count(start[i]) >=2:
                    result = goal
                    return
            result = start[:-2] + start[-1] + start[-2]
            return
        else:
            result = goal
            return

    else:
        for i in range(len(start)):
            if start[i] != goal[i]:
                A.append(i)

        if not len(A)%2:
            if len(A)//2 == cnt:
                result = goal
                return

        a = A.pop(0)
        for j in range(len(goal)-1,-1,-1):
            if goal[a]== start[j]:
                start = start[:a] + start[j] + start[a + 1:j] + start[a] + start[j + 1:]
                cnt -= 1
                SF(start, cnt, goal)
                break


TC = int(input())
for tc in range(1, TC+1):
    card, n = map(str, input().split())
    n = int(n)
    result = 0
    max_card = sorted(card)[::-1]
    max_card = ''.join(max_card)
    SF(card, n , max_card)
    print('#{} {}'.format(tc, result))