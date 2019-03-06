import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    Str = input()
    print('..#..')
    print('.#.#.')
    print('#.{}.#'.format(Str))
    print('..#..')
    print('.#.#.')
