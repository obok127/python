import random

class Baseball:
    def __init__(self):
        self.computer = [-1,-1,-1,-1]
        self.person = [-1,-1,-1,-1]
        self.count = 0
        self.personList = []

    def init_computer(self):
        cnt = 1
        while cnt<=3:
            v = random.randint(0,9)
            if v not in self.computer:
                self.computer[cnt]=v
                cnt +=1

    def init_person(self):
        s = input("숫자 3개를 입력하세요.(예시 0 1 2)")
        numberList = s.strip().split(" ")
        self.person[1]=int(numberList[0])
        self.person[2]=int(numberList[1])
        self.person[3]=int(numberList[2])

    def getResult(self):
        strike = 0
        ball = 0
        out = 0

        for i in range(1,4):
            if self.person[i] in self.computer:
                if self.computer[i] == self.person[i]:
                    strike +=1
                else:
                    ball+=1
            else:
                out +=1
        return strike, ball, out
    
    def start(self):
        flag = False
        self.init_computer()
        print(f"컴퓨터:{self.computer}")
        while flag==False and self.count<=5:
            self.init_person()
            strike, ball, out = self.getResult()
            print(f"strike:{strike} ball:{ball} out:{out}")
            self.personList.append({"person":[x for x in self.person],"strike":strike,
                                    "ball":ball, "out":out})
            if strike == 3:
                flag = True

            self.count+=1

if __name__ == "__main__":
    b = Baseball()
    b.start()

from GameData import Baseball

class GameMain:
    def __init__(self):
        self.gameList = []

    def start(self):
        while True:
            print("1.게임시작")
            print("2.통계")
            print("0.종료")
            sel = input("선택 : ")
            if sel == "1":
                self.gamestart()
            elif sel == "2":
                self.showStatistics()
            else:
                return
    
    def gamestart(self):
        b = Baseball()
        b.start()
        self.gameList.append(b)

    def showStatisitcs(self):
        for b in self.gameList:
            print(b.computer)
            for item in b.personList:
                print(item["person"],item["strike"],item["ball"],item["out"],b.count)

if __name__ =="__main__":
    g = GameMain()
    g.start()

import random

class Baseball:
    def __init__(self):
        self.computer = [-1,-1,-1,-1]
        self.person = [-1,-1,-1,-1]
        self.count = 0
        self.personList = []

    def init_computer(self):
        cnt = 1
        while cnt<=3:
            v = random.randint(0,9)
            if v not in self.computer:
                self.computer[cnt]=v
                cnt +=1

    def init_person(self):
        s = input("숫자 3개를 입력하세요.(예시 0 1 2)")
        numberList = s.strip().split(" ")
        self.person[1] = int(numberList[0])
        self.person[2] = int(numberList[1])
        self.person[3] = int(numberList[2])

    def getResult(self):
        strike = 0
        ball = 0
        out = 0

        for i in range(1,4):
            if self.person[i] in self.computer:
                if self.computer[i] == self.person[i]:
                    strike +=1
                else:
                    ball +=1
            else:
                out +=1
        return strike, ball, out

    def start(self):
        flag = False
        self.init_computer()
        print(f"컴퓨터:{self.computer}")
        while flag==False and self.count<=5:
            self.init_person()
            strike, ball, out = self.getResult()
            print(f"strike:{strike} ball:{ball} out:{out}")
            self.personList.append({"person":[x for x in self.person],
                                    "strike":strike, "ball":ball, "out":out})
            if strike == 3:
                flag = True

            self.count +=1


if __name__ == "__main__":
    b = Baseball()
    b.start()