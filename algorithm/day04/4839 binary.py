import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

def bin_search(P, target):
    start = 1
    end = P
    count = 1
    mid = (start + end) // 2
    while abs(mid -target) >= 1:
        mid = (start + end) // 2
        if mid < target:
            start = mid
            count +=1
        else:
            end = mid
            count += 1

    if mid == target :
        return count
    else:
        return 0

def comp(A,B):
    if A > B:
        return 'B'
    elif A < B:
        return 'A'
    else:
        return 0

T = int(input())

for t in range(1, T+1):
    book = list(map(int, input().split()))
    A = bin_search(book[0],book[1])
    B = bin_search(book[0],book[2])
    result = comp(A,B)
    print(f'#{t} {result}')


