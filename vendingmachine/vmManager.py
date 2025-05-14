#vmManager file
from vmData import VMData
from vmCustomer import VMCustomer
import pickle


class VMManager:
    def __init__(self):
        self.product_list = [
            VMData("Americano", 1000, 10, "25-06-10"), #유통기한은 문자열로

            VMData("Cafe Latte", 2000, 10, "25-06-12"),
            VMData("Milk Tea", 1500, 10, "25-06-11"),
            VMData("Chai Tea", 1500, 10, "25-06-13"),
            VMData("Lemonade", 1500, 10, "25-07-18"),
        ]
        self.customer = VMCustomer(self.product_list)



    def display_menu(self): #class에 따라 메뉴도 나누기  --> feedback : 선입선출 기능(제품명이 동일할 때 어떻게 하면 선입선출을 할 수 있을지)
        print("\n----- 관리자 메뉴 -----")
        print("1.재고확인")
        print("2.유통기한확인")
        print("3.제품추가")
        print("4.제품정보수정")
        print("5.저장")
        print("6.불러오기")
        print("7.제품목록출력")
        print("8.매출 확인")
        print("0.종료")
        print("------------------------")



    def check_stock(self):#1.재고확인
        item_name = input("재고확인할 제품: ")
        result = list(filter(lambda product: item_name.lower() in product.item.lower(),self.product_list))

        if not result:
            print("제품을 찾을 수 없습니다.")
            return

        for product in result:
            print(f"{product.item}는 {product.stock} 개 있습니다.")



    def check_expiry(self):#2.유통기한 확인 --> feedback :유통기한이 다르지만 같은 제품이 입고되었을 경우를 고려
        item_name = input("유통기한 확인할 제품: ")
        result = list(filter(lambda product: item_name.lower() in product.item.lower(),self.product_list))
        if not result:
            print("제품을 찾을 수 없습니다.")
            return

        for product in result:
            print(f"{product.item}의 유통기한은 {product.date}입니다.")



    def add_product(self):#3.제품추가
        item = input("제품명: ")
        price = int(input("제품 가격: "))
        stock = int(input("재고 수량: "))
        date = input("유통기한(YY-MM-DD): ")
        vm = VMData(item, price, stock, date) #vmData로부터 import
        self.product_list.append(vm)
        print("제품이 목록에 추가되었습니다.")



    def modify_product(self):#4.제품정보수정
        item_name = input("수정할 제품명: ")
        result = list(filter(lambda product: item_name.lower() in product.item.lower(),self.product_list))

        if not result:
            print("제품을 찾을 수 없습니다.")
            return

        for i, product in enumerate(result):
            print(f"[{i}] ", end="")
            product.print_info()

        index = int(input("수정할 제품을 고르세요.(숫자로): "))
        selected = result[index]

        selected.item = input("새 제품명: ")
        selected.price = int(input("가격: "))
        selected.stock = int(input("재고수량: "))
        selected.date = input("유통기한 (YY-MM-DD): ")
        print("제품 정보가 업데이트되었습니다.")



    def save_data(self):
        with open("product.bin", "wb") as f:
            pickle.dump(self.product_list, f)
        print("Data saved.")



    def load_data(self):
        with open("product.bin", "rb") as f:
            self.product_list = pickle.load(f)
        print("Data loaded.")



    def view_all(self):
        for product in self.product_list:
            product.print_manager()


    def total_sales(self):
        print("총 판매 금액:", self.customer.total_sales)
        print("제품별 판매 수량:")
        for item, count in self.customer.sales_count.items():
            print(f"{item}: {count}개")



    def start(self):
        while True:
            self.display_menu()
            choice = input("Select: ")

            if choice == "1":
                self.check_stock()
            elif choice == "2":
                self.check_expiry()
            elif choice == "3":
                self.add_product()
            elif choice == "4":
                self.modify_product()
            elif choice == "5":
                self.save_data()
            elif choice == "6":
                self.load_data()
            elif choice == "7":
                self.view_all()
            elif choice == "8":
                self.total_sales()            
            elif choice == "0":
                print("종료")
                break
            else:
                print("잘못된 접근입니다.")


if __name__ == "__main__":
    
    vmM = VMManager()
    vmM.start()
