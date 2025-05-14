import re
contents = """
문의사항이 있으면 010-1234-6789로 연락주시기 바랍니다.
담당자 02-333-4444
국장 02-333-4445
"""
pattern =r'(\d{2,3})-(\d{3,4})-(\d{4})\b'# 전화번호 패턴 정의 (2~3자리)-(3~4자리)-(4자리)
regex = re.compile(pattern)# 정규표현식 컴파일
result = regex.search(contents) # 가장 처음 일치하는 전화번호를 찾음
if result != None:
    phone1 = result.group(1)
    phone2 = result.group(2)
    phone3 = result.group(3)
    print(phone1)
    print(phone2)
    print(phone3)
else:
    print("전화번호가 없습니다.")

    #You're searching for the first phone number and printing its 3 parts.