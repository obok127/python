import re

contents = """
우리커피숍 100-90-12345
영풍문고 101-91-12121
영미청과 102-92-23451
황금코인 103-89-13579
우리문구 104-91-23689
옆집회사 105-82-12345
"""
#내 풀이 : 함수 정의 후 필터함수로 조건에 해당하는 라인 탐색 
pattern =r'(\d{3})-(\d{2})-(\d{5})\b'# 패턴 정의 
regex = re.compile(pattern)# 정규표현식 컴파일

lines = contents.strip().split('\n')  # 줄 단위로 분할


# 필터 함수 정의
def is_valid_business(line):
    result = regex.search(line)
    if result:
        middle = int(result.group(2))
        return 90 <= middle <= 99
    return False

# 필터 적용
valid_lines = list(filter(is_valid_business, lines))

print("조건에 맞는 사업자:")
if valid_lines:
    for line in valid_lines:
        print(line)
else:
    print("는 없습니다.")


