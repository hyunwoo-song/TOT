import sys
sys.stdin = open('input.txt', 'r')

Y, X = map(int, input().split())

if Y ==1:
    cnt = 1
elif Y == 2:
    if X >= 7:
        cnt =4
    else:
        cnt = (X-1)//2 +1
else:
    if X >= 7:
        cnt = 5 + (X - 7)
    elif 3< X and X <7:
        cnt =4
    elif X <=3:
        cnt = X

print(cnt)
