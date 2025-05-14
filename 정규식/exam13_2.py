import re

text1 = " I like star"
text2 = "starship is beautiful"

pattern = "star" #match 함수는 첫부분에 star가 와야한다. 이 문장에서 패턴을 못 찾아냄
print(re.match (pattern, text1)) #None, 뒤에 있어서는 안된다.
print(re.match(pattern, text2))
matchObj = re.match(pattern, text2)
print(matchObj.group())
print(matchObj.start()) #그룹 함수를 통해 단어 추출, 첫번재 패턴의 시작위치 밑 단어의 종료위치, 단어위치 값을 튜플로 나타냄.
print(matchObj.end())
print(matchObj.span())
print(text2[:4])
