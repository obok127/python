#VMCustomer class file
from vmData import VMData
from vmManager import VMManger

class VMCustomer:
    def __init__(self,cash,card,change):
        self.cash = cash
        self.card = card
        self.change = change
        self.pList =[]
        self.process()

    def inputCard(self): #1.입금-카드
        print("카드를 꽂아주세요")
        self.printAll()
        self.choice()
        
    def inputCash(self): #1.입금-현금
        self.cash = int(input("현금을 넣어주세요:"))
        self.printAll()
        self.choice()
        
    def printAll(self): #2.메뉴확인
        for vm in self.productList:
            vm.print()

    def choice(self): #3.제품선택
        item = input("원하는 제품을 고르시오.(숫자만)")
        resultList = list(filter(lambda product: item in product.item, self.productList))
        self.pList.append(resultList)
        
        if len(resultList) == 0:
            print("해당 제품이 없습니다.")
            return
        
        else:
            while True:
                print("1.추가선택")
                print("2.선택종료")
                print("0.구매취소")
                sel = input("선택 : ")
                if sel == "1":
                    self.choice()
                elif sel == "2":
                    self.payment()
                else:
                    return


    def payment(self): #4.결제
        print(f"선택하신 제품은{self.pList}입니다.")
        for i in range(len(self.pList)):
            for j in range():
                self.price += self.productList[2]
        self.process()
        self.print()


    def starting(self):
        while True:
            print("1.카드")
            print("2.현금")
            print("0.종료")
            sel = input("선택 : ")
            if sel == "1":
                self.inputCard()
            elif sel == "2":
                self.inputCash()
            else:
                return


if __name__ == "__main__":
    vc = VMCustomer
    # sm.printAll()
    vc.start()


