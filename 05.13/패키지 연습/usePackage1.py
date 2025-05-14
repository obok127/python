from mypackage1.mymodule2 import isEven, toUpper
# __init__.py랑 mymodule2.py는 mypackage1폴더 안에 있어야 한다
#usepackage1.py(이 파일)는 원래 폴더에 있어야 한다.
print(isEven(10))
print(toUpper("korea"))
