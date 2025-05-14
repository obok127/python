# 다중상속
# 파이썬은 다중상속을 허용한다. 클래스가 동시에 여러 개를 상속받는 경우
# A -> b -> C 중첩 상속 - 모든 언어가 이 구조는 허용한다.
"""
A    B
    C -- 부모 클래스가 A,V인 경우 두 개 이상의 클래스를 상속받는 경우를 다중상속이라고 한다.
        다이아몬드 상속
A -> B --> D
A -> C -- D
        자바는 단일상속만 가능
"""
class Flyable:
    def fly(self):
        print("날 수 있다")


class Swimmable:
    def swim(self):
        print("수영할 수 있다.")

    def walk(self):
        print("*** 두 다리로 걷는다***")


class Duck(Swimmable, Flyable):
    def quack(self):
        print("꽥꽥")


d1 = Duck()
d1.fly
d1.swim()
d1.quack()   
d1.walk() #메소드 명이 동일한 경우에는 앞에 걸 먼저 호출한다.

#시스템이 제공하는 내장변수 중에 __mro__ 가 상속받은 관계정보가 있어서 이걸 따라서 적용한다.
#따라서, 내가 어떤 순으로 상속받는지를 알 수 있다.
print(Duck.__mro__) #클래스 멤버변수로 제공한다

