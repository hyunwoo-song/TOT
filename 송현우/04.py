# 파일명 변경 금지
def cipher(word, n):
    # 아래에 코드를 작성하시오.
    # word는 모두 소문자로만 구성되어 있습니다.
    # n은 양의 정수입니다.
    # 암호화된 문자열을 반환합니다.
    k= [] 
    z= []
    for i in word:
        q= ord(i)+(n%26)
        if ord(i)+(n%26)> 122:
            x = q% 122
            q= x+ 96
        k.append(q)
        

    for y in k:
        z.append(chr(y))
    return ''.join(z)



# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    print(cipher('apple', 1))
    print(cipher('apple', 27))
    print(cipher('zoo', 2))