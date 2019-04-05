


def Go(num, cnt, target):
    global answer, result
    answer += numbers[num]

    if cnt == len(numbers):
        if target==0:
            result += 1
            return
        else:
            return

    Go(num+1, cnt+1, target-numbers[num+1])
    Go(num+1, cnt+1, target+numbers[num+1])


def solution(numbers, target):
    cnt = 0
    Go(-1, cnt, target)

    return result

result = 0
answer = 0
numbers=[1,1,1,1,1]
target=3
print(solution(numbers,target))