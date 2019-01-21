Man1 = input()
Man2 = input()
l = ["가위", "바위", "보"]

if Man1 == l[0]:
    if Man2 == l[0]:
        print('Result : Draw!')
    elif Man2 == l[1]:
        print('Result : Man1 Loss!')
    else:
        print('Result : Man1 Win!')
elif Man1 == l[1]:
    if Man2 == l[1]:
        print('Result : Draw!')
    elif Man2 == l[2]:
        print('Result : Man1 Loss!')
    else:
        print('Result : Man1 Win!')
else:
    if Man2 == l[2]:
        print('Result : Draw!')
    elif Man2 == l[0]:
        print('Result : Man1 Loss!')
    else:
        print('Result : Man1 Win!')



