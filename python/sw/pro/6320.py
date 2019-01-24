x = input()
y = input()
x_g = input()
y_g = input()
result= ''
if x_g == '바위':
    if y_g == '가위':
        result = '바위'
    elif y_g == '보'
        result = '보'

elif x_g == '가위':
    if y_g == '보':
        result = '가위'
    elif y_g == '바위'
        result = '바위'

else:
    if y_g == '바위':
        result = '보'
    elif y_g == '가위'
        result = '가위'

print(f'{result}가 이겼습니다!')
