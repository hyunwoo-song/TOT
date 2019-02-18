import sys

sys.stdin = open('input.txt', 'r')

Arr=list(map(int, input().split()))

N = 11

start = 0
end = len(Arr)-1


while start <= end:
    mid = (start + end) >> 1
    if Arr[mid] == N:
        print('검색성공')
        break
    elif Arr[mid] < N:
        start = mid+1
    else:
        end = mid-1

if Arr[mid] != N:
    print('검색실패')


