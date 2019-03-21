import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    Ex2 = input()
    Ex3 = input()
    L2=[]
    Str2=''
    for i in range(1, len(Ex2)):
        if Ex2[i] == '1':
            Str2 = Ex2[:i]+'0'+Ex2[i+1:]
            L2.append(int(Str2,2))
        else:
            Str2 = Ex2[:i] + '1' + Ex2[i + 1:]
            L2.append(int(Str2,2))


    L3=[]
    Str3=''

    for i in range(len(Ex3)):
        if Ex3[i] == '1':
            Str3 = Ex3[:i]+'0'+Ex3[i+1:]
            L3.append(int(Str3,3))

            Str3 = Ex3[:i] + '2' + Ex3[i + 1:]
            L3.append(int(Str3, 3))

        elif Ex3[i] == '2':
            Str3 = Ex3[:i] + '1' + Ex3[i + 1:]
            L3.append(int(Str3, 3))

            Str3 = Ex3[:i] + '0' + Ex3[i + 1:]
            L3.append(int(Str3, 3))

        else:
            Str3 = Ex3[:i] + '1' + Ex3[i + 1:]
            L3.append(int(Str3, 3))

            Str3 = Ex3[:i] + '2' + Ex3[i + 1:]
            L3.append(int(Str3, 3))

    for l2 in L2:
        if l2 in L3:
            result = l2
            break
    print('#{} {}'.format(t, result))