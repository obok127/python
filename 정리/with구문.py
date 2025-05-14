f = open("mpg.csv","r")
line = f.readlines
print(line[:3])

f = open("mpg.csv","r")
line = f.readlines
print(line[:3])

#파이썬 버전이 낮을 경우에 거듭해서 파일을 여는 거는 안된다.

with open("mpg.csv", "r") as f:
    lines = f.readlines()
    print(lines[:3])

# pickle은 python의 내장 모듈로 객체를 파일로 저장하거나 파일에서 다시 불러올 대 사용
# 객체의 직렬화 , 역직렬화
# serialize/ deserialize
# 객체를 메모리 구조 그대로 파일에 저장
# 파일에서부터 그대로 들고오는 것이 역직렬화

