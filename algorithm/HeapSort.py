# Heap_size = int(input())
# l = []

# for _ in range(Heap_size):
#     l += [int(input())]
#     Mom_node = l[0]
#     son_node_l= l[Heap_size-(Heap_size-1)]
#     son_node_r= l[Heap_size-(Heap_size-2)]
#     if max(Mom_node, son_node_l, son_node_r) == son_node_l:
#         Mom_node , son_node_l = son_node_l, Mom_node
#     elif max(Mom_node, son_node_l, son_node_r) == son_node_r:
#         Mom_node , son_node_r = son_node_r, Mom_node

Heap_size = int(input())
l = []

for _ in range(Heap_size):
    l += [int(input())]
    for index, n enumerate l:
    l_index = 2 * index + 1
    r_index = 2 * index + 2
    if l_index < Heap_size:
        

    if max(Mom_node, son_node_l, son_node_r) == son_node_l:
        Mom_node , son_node_l = son_node_l, Mom_node
    elif max(Mom_node, son_node_l, son_node_r) == son_node_r:
        Mom_node , son_node_r = son_node_r, Mom_node