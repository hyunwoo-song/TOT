l= [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum_i = 0
count =0
while count != 10:
    i = l.pop(0)
    count += 1
    if i >= 80:
        sum_i += i
print(sum_i)