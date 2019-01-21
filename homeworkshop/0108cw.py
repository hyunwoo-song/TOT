def palindrome(string):
    newstring=''
    if len(string)==1:
        print(True)
    else:
        for j in range(-1,-len(string)-1,-1):        
            newstring=newstring+string[j]
        if newstring==string:
            print(True)
        else:
            print(newstring)
            print(False)

palindrome("a")
palindrome("abcdedcba")



def is_palindrom(word):
    if len(word)<2:
        return True
    if word[0]!= word[-1]:
        return False
    return is_palindrom(word[1:-1])