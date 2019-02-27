import sys
sys.stdin = open('input.txt', 'r')
Data = int(input())
print(Data)

mok = Data // 10
na = Data % 10







print(chr(ord('0')+mok)+chr(ord('0')+na))