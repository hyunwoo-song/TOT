import sys
sys.stdin = open('input.txt', 'r')





T = int(input())
for t in range(1, T+1):
    N = int(input())
    Tree=[0]+(list(map(int, input().split())))

    for i in range(len(Tree)):
        while Tree[i] < Tree[i//2] :
            Tree[i], Tree[i // 2] = Tree[i // 2], Tree[i]
            i //= 2

    T_sum = 0
    while N > 0:
        N //= 2
        T_sum += Tree[N]
    print('#{} {}'.format(t, T_sum))


# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     Tree=(list(map(int, input().split())))
#     Tree.append(0x7FFFFFFF)
#     Heap = [0]
#     for i in range(len(Tree)):
#         Heap.append(Tree[i])
#         while Heap[i] < Heap[i//2]:
#             Heap[i], Heap[i//2] = Heap[i//2], Heap[i]
#             i //= 2
#
#     T_sum = 0
#
#     while N > 0:
#         N //= 2
#         T_sum += Heap[N]
#     print('#%d %d'%(t, T_sum))