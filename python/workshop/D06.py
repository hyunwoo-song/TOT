# #1
# def sqrsqr(x):
#     a = 1
#     b = x
#     count = 0
#     while True:
#         if count > 200:
#             break
#         c = (a + b)/2
#         d = c**2
#         if d < x:
#             a = c
#         elif d > x:
#             b = c
#         count += 1
        
#     return (c)
# print(sqrsqr(100)) 


# #2
# def my_sqrt(n):
#     x, y = 1, n
#     result = 1

#     while abs(result**2 - n) > 0.0000001:
#         result = (x+y)/2
#         if result**2<n:
#             x = result
#         else:
#             y = result
#     return result
# print(my_sqrt(100))

#3

def my_sqrt1(n):
    x, y = 1, n
    result = 1
    import math
    while not math.isclose(result**2, n):
        result = (x+y)/2
        if result**2<n:
            x = result
        else:
            y = result
    return result
print(my_sqrt1(100))
