import re

# pattern = r"^abc" #abc로 시작
# pattern = r"abc" #abc가 포함되어야
pattern = r"abc$"  # abc로 끝나야
# This pattern only matches if the string starts with 'ab'.
# If you want to find the exact substring 'abc' anywhere in the text : r"abc"


text = ["abc", "abcd", "abc15", "dabc", "", "s"]
repattern = re.compile(pattern)

for item in text:
    result = repattern.search(item)
    if result:
        print(item, "-O")
    else:
        print(item, "-X")
