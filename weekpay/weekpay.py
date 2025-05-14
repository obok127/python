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


# 파이썬의 모듈들은 내장변수가 있다. __name__
print(__name__)  # 이 모듈로 직접 실행하면 main이 들어온다 python weekpay.py
# import되어 실행되면 파일명이 전달된다. python weekpaymanager.py


# 모듈이 자기 파일 내에서 시작하는 경우 __name__ 내장변수(우리가 만든 게 아니라 시스템이 제공한다.)
# 모든 파일마다 __name__이라는 변수가 존재한다
# 자체적으로 실행할 때는 __name__이고 import되어서 다른 파일이 모듈이 되는 경우 파일명이 온다.
# 각자 클래스를 만들면 각자 테스트 코드를 주고 테스트를 할 때는 이런 식으로 메인...
if __name__ == "__main__":
    w1 = Weekpay("A")
    w1.output()
