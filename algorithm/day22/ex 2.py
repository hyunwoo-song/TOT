import sys
sys.stdin = open('ex2.txt', 'r')


def Bi(num):

    result = ''
    j = ''
    while num:
        j += str(num % 2)
        num //= 2
    for i in range(len(j)-1,-1,-1):
        result += j[i]

    while len(result) < 4:
        result ='0' + result
    return result


A = list(map(str, input()))
s = ''

for a in range(len(A)):
    if ord(A[a])<= 90 and 65 <= ord(A[a]):
        k = ord(A[a]) - 55
        s += Bi(k)
    else:
        s += Bi(int(A[a]))
print(s)

t= 0
for n in range(len(s)):
    t = t*2 + int(s[n])
    if (n+1) % 7 == 0:
        print(t)
        t = 0

if (n+1)%7 !=0:
    print(t)