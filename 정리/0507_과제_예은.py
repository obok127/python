# 가위바위보 게임 -> 객체지향으로
import random


class Game:
    choices = ["", "가위", "바위", "보"]
    results = ["", "컴퓨터 승", "사람 승", "무승부"]

    def __init__(self, person_choice):
        self.person = person_choice
        self.computer = random.randint(1, 3)
        self.winner = self.judge()

    def judge(self):
        if self.person == self.computer:
            return 3
        elif (
            (self.computer == 1 and self.person == 3)
            or (self.computer == 2 and self.person == 1)
            or (self.computer == 3 and self.person == 2)
        ):
            return 1
        else:
            return 2

    def get_result_summary(self):
        return {"person": self.person, "computer": self.computer, "winner": self.winner}

    def print_result(self):
        print(
            f"컴퓨터: {self.choices[self.computer]}, 사람: {self.choices[self.person]}, 결과 : {self.results[self.winner]}"
        )


class GameManager:
    def __init__(self):
        self.history = []

    def play_game(self):
        try:
            person = int(input("1.가위 2.바위 3.보 중 선택: (숫자만 입력하세요)"))
            if person not in [1, 2, 3]:
                print("잘못된 입력입니다.")
                return
            game = Game(person)
            game.print_result()
            self.history.append(game.get_result_summary())
        except ValueError:
            print("숫자를 입력하세요.")

    def show_statistics(self):
        computer_win = sum(1 for g in self.history if g["winner"] == 1)
        person_win = sum(1 for g in self.history if g["winner"] == 2)
        draw = sum(1 for g in self.history if g["winner"] == 3)

        print("\n 게임 통계")
        for idx, game in enumerate(self.history, 1):
            print(
                f"게임{idx}. 컴퓨터: {Game.choices[game['computer']]}, 사람: {Game.choices[game['person']]}, 결과 : {Game.results[game['winner']]}"
            )

        print("\n Total")
        print("컴퓨터 승:", computer_win, "사람 승:", person_win, "무승부:", draw, "\n")

    def start(self):
        myfunctions = {"1": self.play_game, "2": self.show_statistics}
        while True:
            select = input("(1)게임시작 (2)게임통계 (3)게임종료")
            if select in myfunctions.keys():
                myfunctions[select]()
            else:
                print("게임을 종료합니다.")
                break


if __name__ == "__main__":
    manager = GameManager()
    manager.start()


#################################################

import random
class GameData:
    def __init__(self):
        self.computer = 0
        self.person = 0
        self.winner=0

    def gameStart(self):
        self.computer = random.randint(1,3)
        self.person = int(input("1.가위 2. 바위 3.보"))
        self.winner = self.isWinner()

    def isWinner(self):
        s = self
        if s.computer == s.person:
            return 3
        
        if (s.computer==1 and s.person==3) or \
            (s.computer ==2 and s.person ==1) or \
            (s.computer == 3 and s.person == 2):
            return 1
        
        return 2
    
    def printLog(self):
        print(f"컴퓨터{self.computer} 사람: {self.person} 승부 : {self.winner}")

class Game:
    titles1 = ["","가위","바위", "보"]
    titles2 = ["", "컴퓨터승", "사람승","무승부"]

    def __init__(self):
        self.gamelist = []

    def printLog(self,g):
        print(f"컴퓨터 : {self.titles1[g.computer]}",end = "\t")
        print(f"사람 : {self.titles1[g.person]}",end = "\t")
        print(f"승부 : {self.tit}")

