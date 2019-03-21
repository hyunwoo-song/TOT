import sys
sys.stdin = open('1212.txt', 'r')

A= int(input(), 8)
print(bin(A)[2::])