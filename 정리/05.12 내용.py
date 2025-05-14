static메서드 - 본래 메서드도 
class메서드
class Test:
    def __init__(self, number):
        self.number = number
    def output(self):
        print(self.number)

output함수의 매개변수인 self 가 객체를 만들어서 
전달할 때만 사용가능 
대부분의 클래스는 데이터와 함수의 결합이다. 
데이터는 없고 공통이 기능만 갖는 클래스를 만들 수도 있다

class User:
    count = 0

    def __init__(self, username):
        self.username = username
        User.count += 1

    @classmethod
    def from_email(cls, email):
        """이메일에서 사용자 이름만 추출하여 객체 생성"""
        username = email.split('@')[0]
        return cls(username)

    @classmethod
    def get_user_count(cls):
        """생성된 사용자 수 반환"""
        return cls.count


# 사용 예시
print("=== classmethod 예시 ===")
user1 = User("alice")
user2 = User.from_email("bob@example.com")  # 이메일로부터 객체 생성
print("사용자 수:", User.get_user_count())
print("user2 이름:", user2.username)

class TemperatureConverter:
    """섭씨 <-> 화씨 변환: 클래스나 인스턴스 상태와 무관"""

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9


# 사용 예시
print("=== staticmethod 예시 ===")
print("섭씨 25도 -> 화씨:", TemperatureConverter.celsius_to_fahrenheit(25))
print("화씨 77도 -> 섭씨:", TemperatureConverter.fahrenheit_to_celsius(77))

# @staticmethod처럼 @시작한다. 
# 함수의 전후 동작을 감싸서 함수 가로채기를해서 뭔가 작업을 
# 처리하고 원래함수를 호출한다. 

#데코레이터는 함수안에 또 함수를 만든다.(중첩함수)
#매개변수로 받아가서 중첩함수안에서 받아간 함수를 호출한다 
#파이썬에서는 주로 웹에서 많이 사용한다. 
#반드시 로그온을 해야 접근이 가능한 함수를 만들고 싶다. 
#함수를 중간에 가로채서 실행시간 체크를 할 수 있다. 
def decorator1( func ): #매개변수는 중첩함수안에서 호출될함수
    def wrapper():
        print("함수호출전")
        func() 
        print("함수호출후")
    return wrapper #중첩함수의 참조를 반환해야 한다

@decorator1
def hello():
    print("Hello") 

hello() 
#decorator1에게 납치당함 
#->wrapper -> func()를 통해 함수호출
import time 
def time_decorator( callback ):
    def innerfunction():
        start = time.time()
        callback()
        end = time.time() 
        print(f"{callback.__name__} 실행시간 :{end-start}초")
    return innerfunction


@time_decorator
def sigma():
    s=1
    for i in range(1, 10000000):
        s+=i 
    print("합계:",s)

sigma()

#매개변수있고 반환값 있는 경우의 데코레이터 만들기
#callback - 뒤에서 호출한다 
#보통 호출자가 시스템이다. 직접 호출못하고 
#데코레이터한테 사용자 함수를 전달한다.   
def mydecorator(callback):
    #호출될 함수가 어떤 매개변수를 갖고 있는지 알 수 없을경우에
    #tuple타입, dict 타입 매개변수 하나 
    def wrapper(*args, **kwargs):
        result = callback(*args, **kwargs)
        return result 
    return wrapper 

@mydecorator
def add(x, y):
    return x+y 

print( add(5,7))


#데코레이터 만들기 문제 - 로그내보내기 
#@mylog 
#함수를 sigma 매개변수  s = sigma2(10)
"""
[LOG] 함수이름 : sigma2 
[LOG] 입력값 : args = (10), kwargs={}
[LOG] 반환값 : 55 
"""

def mylog( callback):
    def wrapper(*args, **kargs):
        result = callback(*args, **kargs)
        print(f"[LOG] 함수이름 : {callback.__name__}")
        print(f"[LOG] 입력값 : args {args} kwargs {kargs}")
        print(f"[LOG] 반환값 : {result}")
        return result #반드시 반환을 해야 한다 
    return wrapper
        
@mylog 
def sigma2(limit=10):
    s=0
    for i in range(1, limit+1):
        s+=i 
    return s

print( sigma2(100) )
print( sigma2(10) )

@mylog
def sub(a, b):
    return a-b 
print( sub(3, 4) )
