import sys
sys.stdin= open ('input.txt', 'r')

front = 0
rear = 0
hear = 0
Que=[1]* 42
n= 41

for n in range(39):
    hear += 3

    if hear < 42:
        if Que[hear]:
            Que[hear] = 0
        else:
            while Que[hear]:
                hear +=1
            Que[hear] = 0
    else:
        hear = hear % 42
        Que[hear] = 0

print(Que)