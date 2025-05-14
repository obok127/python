import random


class Baseball:
    def __init__(self):  # __init__ 객체가 만들어질 때 딱 한 번 자동으로 실행되는 함수
        # 꼭 써야 하는 건 아니지만, 대부분 이 __init__ 안에서 변수를 세팅한다.
        # self는 지금 만들어진 그 객체 자신
        # self.변수명 : 이 객체가 가진 변수
        # 클래스 :붕어빵 틀, 객체 : 틀로 찍어서 나온 진짜 빵(메모리에 존재함) ->이 코드에서 객체는 b
        self.computer = [
            -1,
            -1,
            -1,
            -1,
        ]  # 값이 할당되지 않았음을 나타낼 때 -1을 사용(아직 숫자 없음)
        self.person = [-1, -1, -1, -1]  # 아무것도 없다
        self.count = 0  # 몇 번 했는지를 저장하기 위한 변수
        self.personList = []

    def init_computer(
        self,
    ):  # Baseball이라는 틀에 있는 init_computer라는 원본 함수를 찾아서 그 함수한테 있는 b라는 객체(붕어빵)를 넘겨줘서 실행
        cnt = 1  # 랜덤값 3개를 추출해야 하는데 3개가 중복되면 안됨.
        while cnt <= 3:
            v = random.randint(0, 9)
            if v not in self.computer:  # 중복아닐때
                self.computer[cnt] = v
                cnt += 1

    def init_person(self):
        s = input("숫자 3개를 입력하세요.(예시 0 1 2)")
        numberList = s.strip().split(" ")
        self.person[1] = int(numberList[0])
        self.person[2] = int(numberList[1])
        self.person[3] = int(numberList[2])

    def getResult(self):
        # 스트라이크, 볼, 아웃 개수
        strike = 0
        ball = 0
        out = 0

        for i in range(1, 4):
            if self.person[i] in self.computer:
                if self.computer[i] == self.person[i]:
                    strike += 1
                else:
                    ball += 1
            else:
                out += 1
        return strike, ball, out

    def start(self):
        # 3strike이거나 5번의 기회를 다 사용했을 경우 종료
        flag = False  # 아직 3strike가 아님을 나타내기 위한 변수
        self.init_computer()
        print(f"컴퓨터:{self.computer}")  # 컨닝페이퍼
        while flag == False and self.count <= 5:
            self.init_person()
            strike, ball, out = self.getResult()
            print(f"strike:{strike} ball:{ball} out:{out}")
            self.personList.append(
                {
                    "person": [x for x in self.person],
                    "strike": strike,
                    "ball": ball,
                    "out": out,
                }
            )
            if strike == 3:
                flag = True

            self.count += 1


if __name__ == "__main__":
    b = Baseball()
    # 이 순간 Baseball 객체가 만들어지면서 __init__() 함수가 자동으로 실행됨.
    # 여기서 b가 객체/인스턴스

    b.start()  # b라는 객체가 가진 start라는 메서드 실행
