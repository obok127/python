class Person:
    # 이 공간은 클래스 공간이다. 클래스 정의할 때 딱 한 번 실행된다.
    # 객체 만들 때마다 실행되지 않는다. 그래서 list타입이나 dict타입 등을 함부로 여기에 선언하면 안된다.
    name = "홍길동"
    age = 12
    phone = [
        "010-0000-0001",
        "010-0000-0002",
    ]  # 공통공간 : 공통변수 사용 시 공통변수 선언

    # 생성자에서 변수를 만들자.
    def __init__(self):  # 객체할 때마다 만들어짐, 파이썬은 생성자에서 변수를 만들어서 사용용
        self.name = ""
        self.age = 0
        self.phone = []

    def append(self, name="임꺽정", age=13, phone="010-0000-0001"):
        self.name = name
        self.age = age

        self.phone.append(phone)

    def output(self):
        print(self.name, self.age, self.phone)


p1 = Person()
p1.append("장길산", 11, "010-0000-0003")

p2 = Person()
p2.append("김종서", 13, "010-0000-0004")

p1.output()
p2.output()

"""
주급 : 이름, 시간당급여액, 근무시간 -> 객체지향으로 한 사람분만
"""


# 내답안
class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_weekly_pay(self):
        return self.hourly_wage * self.hours_worked

    def display_info(self):
        print(f"이름: {self.name}")
        print(f"시간당 급여: {self.hourly_wage}원")
        print(f"주간 근무 시간: {self.hours_worked}시간")
        print(f"주급: {self.calculate_weekly_pay()}원")


name = input("이름은?")
hourly_wage = float(input("시간당 급여는?"))
hours_worked = float(input("주간 근무 시간은?"))

employee = Employee(name, hourly_wage, hours_worked)
employee.display_info()


# 풀이
class Weekpay:
    def __init__(self, name="", work_time=20, per_pay=10000):
        self.name = name
        self.work_time = work_time
        self.per_pay = per_pay
        self.process()  # 클래스 내부 함수 호출 시 self로 해야 한다.

    def process(self):
        self.pay = self.work_time * self.per_pay

    def output(self):
        print(f"{self.name} {self.work_time} {self.per_pay} {self.pay}")


class WeekPayManager:
    def __init__(self):
        self.wList = [
            Weekpay("홍길동", 20, 20000),
            Weekpay("고길동", 10, 50000),
            Weekpay("감길동", 30, 40000),
            Weekpay("이길동", 40, 20000),
            Weekpay("장길동", 20, 20000),
        ]

    def output(self):
        for w in self.wList:
            w.output()

mgr = WeekPayManager() #사용자 입장에서는 Weekpaymanager의 내부 구조는 궁금하지 않음
mgr.output()

#Dto : Data transform object
# 클래스 간에 주고 받은 데이터, 변수, 값, 계산(한 사람 분량)
#DB기준 테이블 
# 변수는 텍배상자

#DAO(data access object 파일 데이터 읽고 쓰기)

#구조적 프로그래밍 - 양옥집
#객체지향 - 조립식 주택을 만들기 위한 부품 제작



"""
w1 = Weekpay("홍길동", 20, 20000)
w1.output()

wList = [
    Weekpay("홍길동",20,20000),
    Weekpay("고길동",10,50000),
    Weekpay("감길동",30,40000),
    Weekpay("이길동",40,20000),
    Weekpay("장길동",20,20000)
]

for w in wList:
    w.output()
"""
