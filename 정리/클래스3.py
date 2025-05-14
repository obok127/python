class Book:
    title = "채식주의자"

    def __init__(
        self, title="쌍갑포차", paramprice=10000
    ):  # 왜 기본값을 줄까? 객체 생성방법을 다원화하기 위해서 : 매개변수에 기본값을 안 주면 Book()만 쓸 수 있는데, Book("메롱") 이런식으로 다양하게 사용 가능
        print("self", self)  # 객체주소 : 실제 주소는 아니고 가상의 주소
        self.title = title  # self를 쓰지 않으면 클래스를 쓰는 의미가 없다.
        # self를 이용해서 생성자쪽에서 꼭 안해도 변수를 만들어서 붙일 수 있다
        self.price = paramprice  # 이 때 price는 지역변수이다. 함수가 끝나면 사라짐, 클래스 변수가 아님
        self.count = 10
        self.process()  # 함수도 매개변수로 self를 받아가야 한다.

    def process(self):
        self.total_price = (
            self.price * self.count
        )  # 클래스 전체에서 값이 유지되고 싶으면 self를 붙여야 한다. 필요하면 이런 식으로 변수 선언 가능
        # 그냥 매개변수로 받는 게 생성자 단계에서 받는 것

    def output(self):
        print(self.title, self.price, self.count, self.total_price)

    pass


b = Book()  # 객체가 만들어진다.
# title이라는 클래스 내부 변수에 접근하려면 접근연산자로 .(도트)
print(b)
print(b.title)
print(
    b.price
)  # b가 self로 전달 근데 price는 셀프로 안줬으니까 이걸 받아들이지 못함. 그래서 이게 클래스 변수가 아니라서 price가 없다고 나옴.

b2 = Book("아 지갑놓고 나왔다")
print(b2)
print(b2.title)

b3 = Book("뽀짜툰", 30000)
print(b3)  # self에 계속 다른 주소가 담긴다. self는 객체 주소가 전달되어지는 변수
# 예외적으로 메서드가 객체에 속하지 않을 때, 클래스에 속한 클래스 메소드의 경우(자바에서는 static) self를 사용하지 않는다.
# 공통적인 건 없는데
# Math.round/sin/cos/tan : 수학함수들끼리 데이터를 공유하지는 않지만 묶어놓았을 때 사용하기 편하다. 그러면 공유되는 데이터가 없고, 객체를 굳이 만들 필요가 없기 때문에,
# 이 안에 들어가는 메소드는 self가 없다. 굉장히 드문 일
# 누구한테나 다 필요할 것 같은 함수인데 종속적이지는 않은 그런 함수들, 특정 클래스에 종속시키기에는 불편할 것 같은 경우, 필요에 따라 클래스를 새로 만들어서 필요로 하는 함수들만 모아놓음.
# self를 붙여야 객체의 주소를 받을 수 있고, self를 안 받는 경우는 굉장히 예외적인 일
# keras에서 class, 객체지향을 사용하기 때문에 클래스를 배움..
# 웹개발 장고는 클래스 기반임

print(b3.title)

# 파이썬은 title이 하나로, 자바는 하나씩 title이 다 생김 이 때, 자바처럼 하고 싶으면 생성자를 써야 함.
# 그 때, self.title을 사용하는데 self에 객체 주소를 받음. 그래서 self.title이 b1의 title이, b2의 title이 됨 즉, self가 b1, b2, b3가 될 수 있다
# 꼭 self일 필요는 없는데 그냥 묵시적으로 사용
# 자바의 경우 이미 시스템에서 되기 때문에 안 넣어도 되는데, 파이썬을 경우 직접 넣어줘야 함.
# 첫번째 오는 변수가 객체 주소를 받는다!!
# self에 붙이지 않으면 그냥 지역변수가 됨

# 변수는 별개의 메모리를 사용하지만 함수는 메모리를 같이 쓴다.그래서 self.함수명
