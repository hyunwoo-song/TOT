import sys
sys.stdin = open('ex3.txt', 'r')

P ={
    0:'001101',
    1:'010011',
    2:'111011',
    3:'110001',
    4:'100011',
    5:'110111',
    6:'001011',
    7:'111101',
    8:'011001',
    9:'101111'
}

A = int(input(), 16)
B = str(bin(A)[2::])
result = '0000'+ B
i = 0

while i < len(result)-5:
    for k,v in P.items():
        if result[i:i+6]==v:
            i +=6
            print(k)
    i += 1


