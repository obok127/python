#가위바위보 게임
import random

class GameData: - computer, person, 승부여부
    #변수 선언을 생성자에서 하자. : 그래야 객체가 생성될 때마다 새로운 메모리를 만들어준다.
    def __init__(self):
        self.computer = 0
        self.person = 0
        self.winner=0

    def gameStart(self):
        self.computer = random.randint(1,3)
        self.person = int(input("1.가위 2. 바위 3. 보"))
        self.winner = self.isWinner()
    
    def isWinner(self):
        s = self
        if s.comuter == s.person:
            return 3 #무승부
        #명령어가 한 문장 이상일 때 연결하는 문자 \ 양쪽에 공백 필요함
        if (s.computer == 1 and s.person == 3) or \
            (s.computer == 2 and s.person == 1) or \
            (s.computer == 3 and s.person == 2) :
            return 1 #컴퓨터 승
        
        return 2 #사람 승

    def printLog(self):
        print(f"컴퓨터{self.computer} 사람 : {self.person} 승부 : {self.winner}")

if __name__ =="__main__":

    g = GameDate() #객체 생성
    g.gameStrat() #g ->self로 전달된다
    g.printLog()

