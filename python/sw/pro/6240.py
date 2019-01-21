sum_i = 0
for i in range(1, 101):
    if not i % 3:
        sum_i += i
print(f'1부터 100사이의 숫자 중 3의 배수의 총합: {sum_i}')
