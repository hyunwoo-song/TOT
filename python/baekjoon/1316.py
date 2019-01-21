N = int(input())
count = 0
for i in range(N):
    c = 0
    word = input()
    sample_word = word[0]
    l=[]
    for n in range(len(word)-1):
        if sample_word != word[n+1]:
            l += [sample_word]
            sample_word= word[n+1]
            if word[n+1] in l:
                c -= 1
    c += 1
    if c == 1:
        count += c
    
print(count)
        