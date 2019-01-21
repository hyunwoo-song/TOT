s = input()
S= s.upper()
count = 0
max_count= 0
result_string = ''
l =['A','B','C','D','E','F','G','H','I','J','K','L',
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W',
    'X', 'Y', 'Z']

for i in l:
    if i in S:
        count = S.count(i)
        if count > max_count:
            max_count = count
            result_string = i
        elif count == max_count:
            result_string = '?'
print(result_string)