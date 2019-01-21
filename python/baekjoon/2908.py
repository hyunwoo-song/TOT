num_1, num_2 = input().split()
n1 = num_1[::-1]
n2 = num_2[::-1]
if int(n2) > int(n1):
    print(n2)
else:
    print(n1)