import sys
sys.stdin = open('input.txt', 'r')

T = 1
for t in range(1, T+1):
    N = int(input())
    Tree=[0]*(N+1)
    for n in range(N):
        List = list(input().split())
        Tree[int(List[0])] = List[1]
    sum =0
    print(Tree)
    while len(Tree) >2:
        M=len(Tree)-1
        if Tree[M].isdigit() and Tree[M-1].isdigit():
            if Tree[M // 2] == '/':
                Tree[M // 2] = str(int(Tree[M-1]) // int(Tree[M]))
            elif Tree[N // 2] == '*':
                Tree[N // 2] = str(int(Tree[M-1]) * int(Tree[M]))
            elif Tree[N // 2] == '+':
                Tree[N // 2] = str(int(Tree[M-1]) + int(Tree[M]))
            elif Tree[N // 2] == '-':
                Tree[N // 2] = str(int(Tree[M-1]) - int(Tree[M]))
            Tree.pop(-1)
            print(Tree)
            Tree.pop(-1)

        else:
            break


    if len(Tree) == 2:
        sum=Tree[-1]
    print('#{} {}'.format(t, sum))
