import os

print("Current working directory:", os.getcwd())
# 딥러닝 때 shutil 사용함
import shutil

shutil.copy("./내장함수2.py", "./내장함수3.py")
# 주로 move나 copy를 많이 씀
# 디렉토리 문제가 나오면 ~\Desktop\예은❯ cd .\05.13

import glob

filelist = glob.glob("c:/*")
print(filelist)

import glob

filelist = glob.glob("./*.py")
print(filelist)


import os

print(os.environ)
print(os.environ["PATH"])

print(os.getcwd)  # 현재 내가 있는 경로를 보여줌

# 파이썬에서 os명령어를 쓰고 싶을 때
os.system("dir/w")
