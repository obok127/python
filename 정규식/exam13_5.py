import re

text ="""
    phone : 010-0000-0000 email:test1@nate.com
    phone : 010-1111-1111 email:test2@naver.com
    phone : 010-2222-2222 email:test3@gmail.com
    phtone: 02-345-9090 email:dseisk@hanmail.net    
"""

print()
print("--- 전화번호 추출하기 ---")
phonepattern = r"\d{2,3}-\d{3,4}-\d{4}"

matchObj = re.finditer(phonepattern, text) #반복자 변환

for item in matchObj:
    print( item.group() ) 
    print(item.span())
print()