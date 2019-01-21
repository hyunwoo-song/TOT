cro_str = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
S = input()
count = 0
K = 0
for i in cro_str:
    if i in S:
        count += S.count(f'{i}')
        S = S.replace(f'{i}', '_')
        K = len(S)-S.count('_')
if not S.count('_'):      # 리스트의 단어가 없을때 
        K = len(S)
count += K
        
print(count)