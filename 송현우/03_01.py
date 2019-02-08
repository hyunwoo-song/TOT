# 파일명 변경 금지
def alphabet_count(word):
    # 아래에 코드를 작성하시오.
    # word는 소문자로만 구성 되어있습니다.
    # 딕셔너리를 반환합니다.
    a = word
    l=[]
    c=[]
    for i in a:
        if not i in l:
            l.append(i)
            k = a.count(i)
            c.append(k)
            d= dict(zip(l,c))
    return d
        








# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    print(alphabet_count('hello'))
    print(alphabet_count('internationalization'))
    print(alphabet_count('haha'))