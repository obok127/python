#VMManager class file
from vmData import VMData

import pickle

class VMManager:
    def __init__(self):
        self.productList =[
            VMData("Americano", 1000, 10, 25-06-10),
            VMData("Cafe Latte", 2000, 10, 25-06-12),
            VMData("Milk Tea", 1500, 10, 25-06-11),
            VMData("Chai Tea", 1500, 10, 25-06-13),
            VMData("Lemonade", 1500, 10, 25-07-18)  
        ]

    def menuDisplay(self):
        print("------------")
        print("     메뉴    ")
        print("------------")
        print("   1.입금    ")
        print("  2.메뉴확인  ")
        print("  3.제품선택  ")
        print("   4.결제    ")
        print("------------")
        print(" 관리자 메뉴 ")
        print("------------")
        print(" 5.재고 확인 ")
        print(" 6.유통기한확인 ")
        print("  7.제품추가  ")
        print(" 8.제품정보수정 ")
        print("    9.저장    ")
        print("  10.불러오기  ")
        print("   0.종료    ")


    def find(self): #5.재고확인
        item = input("재고확인할 제품 : ")
        resultList = list(filter(lambda product: item in product.item, self.productList))
        if len(resultList) == 0:
            print("데이터가 없습니다.")
            return
        
        for item in resultList:
            a = resultList[0]
            b = resultList[2]
            print(f"{a}는 {b}개 있습니다.")
        

    def check(self): #6.유통기한확인
        item = input("유통기한 확인할 제품 : ")
        resultList = list(filter(lambda product: item in product.item, self.productList))
        if len(resultList) == 0:
            print("데이터가 없습니다.")
            return
        
        for item in resultList:
            a = resultList[0]
            b = resultList[3]
            print(f"{a}의 유통기한은 {b}입니다.")        

    def append(self): #7.제품추가
        vm = VMData()
        vm.item = input("제품명: ")
        vm.price = int(input("제품가격: "))
        vm.stock = int(input("재고수량: "))
        vm.date = int(input("유통기한: "))
        print("추가되었습니다.")
        self.productList.append(vm)

    def modify(self): #8.제품정보수정
        item = input("수정할 제품 : ")
        resultList = list(filter(lambda product: item in product.item, self.productList))
    
        if len(resultList) == 0:
            print("찾으시는 데이터가 없습니다.")
            return

        for i, v in enumerate(resultList):
            print(f"[{i}]", end=" ")
            v.print()

    def save(self): #9.저장
        with open("product.bin", "wb") as f:
            pickle.dump(self.productList, f)
        print("저장되었습니다")

    def load(self): #10.불러오기
        with open("product.bin", "rb") as f:
            self.productList = pickle.load(f)
        self.printAll()


    def start(self):
        funcList = [
            None,
            self.input,
            self.printAll,
            self.choice,            
            self.payment,
            self.find,
            self.check,
            self.append,
            self.modify,
            self.save,
            self.load,
        ]
        while True:
            self.menuDisplay()
            choice = int(input("선택 : "))
            if choice > 0 and choice < len(funcList):
                funcList[choice]()
            elif choice == 0:
                return
            else:
                print("잘못된 선택입니다.(숫자만 0~10)")


if __name__ == "__main__":
    vmM = VMManager()
    # sm.printAll()
    vmM.start()


