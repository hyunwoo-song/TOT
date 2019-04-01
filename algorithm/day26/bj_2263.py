import sys
sys.stdin = open('2263.txt')

N = int(input())
j = 2
cnot = 1

while j< N:
    j *= 2
    cnot += 1

Order = [0]*j

In_O = list(map(int, input().split()))
Post_O = list(map(int, input().split()))

Order[2**(cnot-1)] = Post_O[0]
left = Post_O[0]
top = [Post_O[-1]]
Order[1] = top[-1]
end = []
cnt = True
right = [Post_O[len(Post_O)-2]]


u = 1
while cnt:
    cnt = True

    for i in range(N):
        if In_O[i] == top[-1]:
            end.append(In_O[i+1])
            right.append(In_O[i-1])
            break

    for ii in range(N):
        if Post_O[ii] == end[-1]:
            top.append(Post_O[ii-1])
            Order[2**u] = top[-1]
            u +=1
            break

    if In_O[1] == top[-1]:

        cnt = False



