import sys
sys.stdin=open('5202')

T= int(input())
for tc in range(1, T+1):
    N = int(input())

    Table = [1] * 25
    cnt =0
    Time=[(list(map(int, input().split()))) for n in range(N)]
    Z=0
    max_s=0
    while Time:

        min_e = 0x7FFFFFFF
        max_i = 0

        for j in range(len(Time)):
            if min_e >= Time[j][1]:
                min_e = Time[j][1]
                max_s = Time[j][0]
                max_i = j
        K = Time.pop(max_i)
        if max_s >= Z:
            cnt +=1
            Z= min_e
    print(cnt)





