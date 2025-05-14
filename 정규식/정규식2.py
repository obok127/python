import re
pattern = r"비" #패턴은 문자열 \ - 이건 기본적으로 escape로 사용을 한다. 패턴에서는 문자열로 써야 한다.
                # \의 exscape 기능을 무력화 해야 한다. 
                #따라서 패턴 문자열 앞에 r을 붙여야 한다.

text = """
하늘에서 비가 오고 있습니다.
어제도 비가 왔고,
오늘도 비가 오고 있습니다.
"""

regex = re.compile(pattern) #

result = regex.findall(text)

print(result) #다음은 b가 몇번 등장합니까 같은 걸 물어