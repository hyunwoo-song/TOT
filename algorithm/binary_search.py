def binary_search(max_num, answer):
    min_num = 0
    mid_num = (max_num + min_num) // 2
    count = 1
    while answer !=  mid_num:
        if answer < mid_num:
            max_num = mid_num 
            mid_num = (max_num + min_num) // 2
            count +=1
        
        elif answer > mid_num:
            min_num = mid_num
            mid_num = (max_num + min_num) // 2
            count +=1
    return count
        
print(binary_search(100, 31))
