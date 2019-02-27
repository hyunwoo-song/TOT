import sys
sys.stdin = open('input.txt', 'r')

Data = list(input())
print(Data)

val = Data[0]


for d in range(len(Data)):
    if '0' <= Data[d]and Data[d] <= '9':
        val += ord(Data[d])-ord('0')

    elif 'A' <= Data[d]and Data[d <= 'F':
        val += (ord(Data[d])-ord('A'))+10