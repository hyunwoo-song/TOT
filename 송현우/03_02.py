# 파일명 변경 금지
def alphabet_mode(word):
    # 아래에 코드를 작성하시오.
    # word는 소문자로만 구성 되어있습니다.
    # word에서 가장 많이 발생한 알파벳 하나를 반환합니다.
    a = word
    result = ''
    max_count = 0 
    for i in a:
        k = a.count(i)
        if max_count < k:
            max_count = k
            result = i
    return result




# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    print(alphabet_mode('hello'))
    print(alphabet_mode('internationalization'))
    print(alphabet_mode('haha'))