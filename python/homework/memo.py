# def calc(equation):
#     s= equation.replace('+', ' +')
#     s1= s.replace('-', ' -')
#     return sum(map(int, s1.split()))




# print(calc('123+2-124'))
# # print(calc('-12+12-7979+9191'))
# # print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))

T = int(input())
print(f'{T:0.2f} inch => {T * 2.54} cm')