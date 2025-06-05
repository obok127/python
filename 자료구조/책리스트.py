class Node:
    def __init__(self, data = None):
        self.data = data #데이터 파트
        self.next = Node #다음 번 요소의 주소를 줘야 함.

class Book:
    def __init__(self, title="", author="",publisher=""):
        self.title = title
        self.author = author
        self.publisher = publisher
    
    def __gt__(self, other): #연산자 중복 : 클래스 객체들끼리 연산자(>, <, ==, +, - 등)를 사용할 때,그 연산의 의미를 직접 정의하는 것
        return self.title > other.title

    def __str__(self): #출력할 때 문자열 전환하는 방법 기억해두기
        return f"{self.title}, {self.author},{self.publisher}"

class BookList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.next = self.tail

    def insertOrder(self,title, author, publisher):
        new_book = Book(title, author, publisher)
        temp = Node(new_book)
        #1. 위치 찾기
        t1 = self.head.next
        t2 = self.head 
        flag = False

        while not flag and t1!= self.tail:
            if t1.data > temp.data:  
                flag = True 
            else:
                t1 = t1.next
                t2 = t2.next

        temp.next = t1
        t2.next = temp

    def print2(self):
        current = self.head.next
        while current != self.tail:
            print(current.data)
            current = current.next

print( Book("마법사의돌", "조앤롤링", "해냄"),
       Book("그리고아무도없었다", "아가사크리스티", "해냄"))

b1 = BookList()    
b1.insertOrder("나무","베르나르베르베르","뫼비우스")
b1.insertOrder("작별하지않는다","한강","문학동네")
b1.insertOrder("젊은베르테르의슬픔","요한볼프강폰괴테","민음사")
b1.insertOrder("브람스를좋아하세요","프랑수아즈사강","민음사")
b1.insertOrder("젊은예술가의초상","제임스조이스","민음사")
b1.print2()

"""
***코드 설명***
Node 클래스는 연결리스트의 기본 단위인 노드를 정의
각 노드는 Book 객체를 가지고, 다음 노드의 참조를 가짐.

Book 클래스는 제목, 저자, 출판사를 속성으로 가지며,
두 Book 객체를 > 연산자로 비교할 수 있도록 연산자 중복을 정의__gt__
출력할 때 문자열 형태(타이틀, 저자, 출판사)로 바꿈__str__

BookList 클래스 - insertOrder 메서드는 연결리스트를 만들어서,Book 객체를 정렬된 순서로 삽입
새로운 Book을 삽입할 때, 현재 리스트를 순회하며 어디에 넣어야 할지 찾고(비교 연산자 중복으로),찾아낸 위치에 노드를 삽입
"""
"""
단순히 데이터를 저장하고 조회만 한다면 파이썬 리스트가 편리
중간에 자주 데이터를 추가하거나 삭제할 일이 많다면 링크드 리스트가 더 적합
"""


b1 = Book("쌍갑포차")
b2 = Book("쌍갑포차")
print( b1 == b2 ) # 참조비교 - False가 출력
#b1과 b2의 내용 비교가 아니고,
#b1이 참조만 저장, b2도 참조만 저장
#둘이 동일한 객체를 참조하고 있는가?
# "hello".equals(temp)
#객체는 참조용 변수라서 내용 비교를 하려면 연산자 중복을 사용해야 함
s1 = str("hello")
s2 = str("hello")
print( s1 == s2 ) #내용비교 - True가 출력
#str은 내부적으로 내용을 비교하도록 해놓음


