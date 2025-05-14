# 짝수면 True 홀수면 False 반환
def isEven(x):
    if x % 2 == 0:
        return True
    return False


def toUpper(word):
    return word.upper()

def toUpper1(s):
    # A -65 a-97 둘 사이에 32만큼 소문자를 대문자로 -32,대문자를 소문자로 +32
    temp=""
    for c in s:
        if ord(c)>=ord('a') and ord(c)<=ord('z'): #소문자일 때
            c = chr(ord(c)-32) #'a' - 97 -32 = 65 -> 문자로 바꾼다
        temp = temp + c #소문자가 아닌 것(대문자)이 오면 그냥 더한다.
    return temp

# def toUpper2(word_list):
#     new_list = []
#     for w in word_list:
#         new_list.append(w.capitalize)
#     return (new_list)

# def toUpper3(word_list1):
#     return [w.capitalize() for w in word_list1]

# def toUpper4(word):
#     new_list = []
#     for char in word:
#         new_list.append(char.upper())
#     return new_list

# def toUpper5(word):
#     return [char.upper() for char in word]


if __name__ == "__main__":
    print(isEven(4))
    print(toUpper("asterisk"))
    print()
    print(toUpper1("asterisk"))


