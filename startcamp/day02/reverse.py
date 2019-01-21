# write
with open('ssafy.txt','w',encoding='utf8') as f: # with 
    f.writelines(['1\n','2\n','3\n'])
    

# read  
with open('ssafy.txt','r',encoding='utf8') as f:
    lines = f.readlines()
    lines.reverse()

    for line in lines:
        print(line.strip()) 

#write
    with open('ssafy_reverse.txt','w',encoding='utf8') as n:
            n.writelines(lines)
       


########################정 답########################
# 1. 한번에 처리
#  with open('ssafy.txt','r',encoding='utf8') as f:
#     lines = reversed(f.readlines())
#     or lines.reverse()

#     with open('ssafy_reverse.txt','w',encoding='utf8') as ff:
#         ff.writelines(lines)


# # 2. read/ write
# with open('ssafy.txt', 'r',encoding='utf8') as f:
#     lines = f.readlines()

# lines.reverse()

# with open('ssafy_reverse.txt','w',encoding='utf8') as f:
#     f.writelines(lines)