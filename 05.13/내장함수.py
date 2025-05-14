print(abs(-4))
print(abs(4))
print()
print(all([1, 2, 3]))  # 지금 전달받은 요소 중에 0이 하나라도 존재하면 False
print(all([1, 2, 3, 0]))  # 요소 전체가 True이면 Ture (0, "" - False)
print(all(["a", "b", "c"]))
print(all(["a", "b", ""]))
print()
print(any([1, 2, 3]))  # 지금 전달받은 요소 중에 0이 아닌 것이 하나라도 존재하면 True
print(any([1, 2, 3, 0]))
print(any([0, 0]))
print(any([1, 2, ""]))
print(any(["", ""]))

############################
print(dir([1, 2, 3]))
print()  # 객체가 지닌 변수나 함수를 보여 주는 함수
print(dir(dict()))
print()
quotient, remainder = divmod(5, 3)
print(quotient)
print(remainder)


for i, c in enumerate("Life is Egg"):  # 문자열, 튜플, set, list, dict
    print(i, c)
print()
result = eval("1+10+3")
print(result)
print()
result = eval("(1+10)*2-3")
print(result)

a = [3, 4, -1, 2, 9, 8, 7, 12, 15, 21]


# 음수만 : filter의 첫번째 매개변수는 함수여야 한다.
# 두번째 매개변수로 전달된 요소 하나를 매개변수로 하고 반환은 True 또는 False
def isPositive(x):
    if x > 0:
        return True
    return False


poList = filter(isPositive, a)
print(list(poList))


print()
# 한번 만들어서 쓰고 버리는 함수인 람다를 사용하자.
poList = list(filter(lambda x: x > 0, a))
print(poList)

print(f"최대값 {max(a)} 최소값{min(a)}")
print()
print(pow(2, 4))

# 컴퓨터는 시간을 1970년 1월 1일을 기산점으로 초당 1씩 카운트
import datetime

day1 = datetime.date(2021, 12, 12)
day2 = datetime.date(2023, 4, 5)
print(day1)
print(day2)

day3 = day2 - day1  # timedelta 객체로 바뀌고 날짜를 갖고 있다.
print(day3.days)
print()
# 말일까지 몇일이 남았는가
day1 = datetime.date(2025, 5, 13)
day2 = datetime.date(2025, 5, 31)
day3 = day2 - day1  # timedata 객체로 바뀌고 날짜를 갖고 있다.
print(day3.days, "일")
print()
day1 = datetime.date(2025, 5, 13)
day2 = datetime.date(2025, 12, 31)
day3 = day2 - day1  # timedelta 객체로 바뀌고 날짜를 갖고 있다.
print(day3.days, "일")
############################
print()

# 말일까지 몇일이 남았는가?
# 연도랑 월을 주면 말일을 계산해주는 라이브러리가 있다.
import calendar
from datetime import date

# 오늘 날짜를 구한다.
today = date.today()
year = today.year
month = today.month

# tuple 해당 월의 첫째날과 마지막날

last_day = calendar.monthrange(year, month)[1]
print(last_day)

day1 = datetime.date(year,month, last_day)
print( (day1-today).days)
############################
print()

#오늘은 무슨 요일
print(today.weekday())
#0 1 2 3 4 5 6  월화수목금토일

#문제: 날자를 입력을 받아서 그날이 무슨 요일인지 반환하는 함수 만들기
#"2025-05-11"

# today_ = input("yyyy-mm-dd")
# a=today_.weekday()
weekdays ={"0":"월","1":"화","2":"수","3":"목","4":"금","5":"토","6":"일"}
############################
print()


from datetime import datetime #import datetime만 하면 아래에 datetime 두번
#내가 짠 코드
s = input("yyyy-mm-dd")
today_date = datetime.strptime(s,"%Y-%m-%d").date()
a= today_date.weekday()

weekdays ={0:"월",1:"화",2:"수",3:"목",4:"금",5:"토",6:"일"}

if a in weekdays:
    print(weekdays[a])



#"2025-05-11" Y-연도자리 y-연도2자리 - 문자열을 date로 받는 법
# day1 = datetime.strptime("2025-05-12","%Y-%m-%d")
# print(day1.weekday())


#선생님이 짜신 코드
def getWeekday(s): #클래스에서 스태틱 메서드로 만들어두면 여러 사람이 활용할 수 있음.
    day1 = datetime.strptime(s,"%Y-%m-%d")
    weekday = day1.weekday()
    titles = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
    return titles[weekday]

print(getWeekday("2025-05-12"))


# random.randint(1, 10) 얘는 1~10까지 포함임 보통은 끝자리를 포함하지 않지만

############################
print()

# # 딥러닝 때 shutil 사용함
# import shutil

# shutil.copy("./연습.py", "./연습2.py")
# # 주로 move나 copy를 많이 씀


import shutil
import os

# Check current working directory
print("Current working directory:", os.getcwd())

# Try copying the file using absolute paths
shutil.copy("C:/Users/user/Desktop/예은/05.13/연습.py", "C:/Users/user/Desktop/예은/05.13/연습2.py")


import os
os.chdir("C:/Users/user/Desktop/예은")
shutil.copy("./연습.py", "./연습2.py")