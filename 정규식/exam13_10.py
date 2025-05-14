import re

# ? - 없거나 하나만 있거나 (*,?는 많이 쓰지 못함.)
# + - 패턴이 하나 이상 반복
# * - 없거나 하나이상 반복

patterns =[r"\d?", r"\d+", r"\d*"]#정수 하나 있고 문자 하나 있는 패턴을 찾는다.
text = ["abc","1abc","12abc","123","aa12ab"]

for pattern in patterns:
    resultList = []
    for item in text:
        result = re.search(pattern, item)
        if result == None:
            resultList.append(item+"-X")
        else:
            resultList.append(item +"-O")
        
    print(resultList)