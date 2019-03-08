import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    Strings = [list(map(str, input())) for _ in range(5)]
    max_S =0
    result=''
    for i in range(5):
        if max_S < len(Strings[i]):
            max_S = len(Strings[i])

    for i in range(5):
        while max_S != len(Strings[i]):
            Strings[i].append('')
    NStrings=list(map(list, zip(* Strings)))
    for i in range(max_S):
        for j in range(5):
            result += NStrings[i][j]
    print('#{} {}'.format(t, result))

print(NStrings)