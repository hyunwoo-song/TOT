import sys
sys.stdin= open('code.txt', 'r')

P=['1123','1222','2212','1141','2311','1321','4111','2131','3121','2113']

T= int(input())
for t in range(1, T+1):
    Y = ''
    N, M = map(int,input().split())
    Arr=[list(map(str, input().split())) for n in range(N)]
    R = ''
    flag = False
    RResult = 0
    for n in range(N):
        for m in range(M):
            while Arr[n][0][m] != '0':
                R+=Arr[n][0][m]
                m += 1
                flag = True

            if flag:
                break
    print(R)
    result= bin(int(R, 16))[2::]
    while len(result) < len(R)*4:
        result = '0'+result
    z = len(result)//56


    for hh in range(len(result)-1,-1,-1):
        if result[hh] == '1':
            hhh= len(result)-1-hh
            break

    kesult = '0'*hhh+ result[0:len(result)-hhh]
    print(kesult)
    r = len(kesult)-1
    while 0 < r:
        q = ''
        if kesult[r] == '1':
            O = kesult[r-(7*z)+1:r+1]
            print(O)
            cnt = 0
            h = '1'
            o = len(O)-1
            while o >= 0:
                while O[o] == h:
                    cnt +=1
                    o -= 1
                h = O[o]
                q += str(cnt)
                cnt = 0

            for i in range(len(P)):
                if P[i] == q:
                    Y += str(i)

            r-= (7*z -1)
        r -= 1
    print(Y)
    RRR=int(Y[0])+(int(Y[1])+int(Y[3])+int(Y[5])+int(Y[7]))*3 +(int(Y[2])+int(Y[4])+int(Y[6]))
    if not RRR % 10:
        for kk in range(len(Y)):
             RResult += int(Y[kk])
    print('#{} {}'.format(t, RResult))
