T = int(input())

for _ in range(T):
    S = input()
    for i in range(10):
        new_S = S.replace(S[:i+1], (' '*(i+1)))
        len_S = len(S[:i+1])
        count_S = new_S.count(' ')
        new_S2 = new_S.split(' ')
        if count_S == 30:
            result = i+1
            break
        
        elif count_S == (len_S*(30//len_S)):
            result = len_S
            break
    print(f'#{_+1} {result}')

# KOREAKOREAKOREAKOREAKOREAKOREASAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
# GALAXYGALAXYGALAXYGALAXYGALAXY




# BLACKPINKBLACKPINKBLACKPINKBLA

# REDVELVETREDVELVETREDVELVETRED