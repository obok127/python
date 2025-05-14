# vmCustomer file
from vmData import VMData


class VMCustomer:
    def __init__(self, product_list):
        self.product_list = product_list
        self.cash = 0
        self.card = 0
        self.cart = []
        self.total_sales = 0
        self.sales_count = {p.item: 0 for p in product_list}
        self.sc = []

    def print_menu(self):  # 제품 목록 출력
        print("----- Product List -----")
        for vm in self.product_list:
            vm.print_customer()
        print("------------------------")

    def howtopay(self):  # 1.결제방식선택
        while True:
            print("\n--- 결제방식 선택 ---")
            print("1.현금 결제")
            print("2.카드 결제")
            choice = input("Select: ")
            if choice == "1":
                self.input_cash()
                break
            elif choice == "2":
                self.input_card()
                break
            else:
                print("유효하지 않은 접근입니다. 다시 시도해 주세요.")

    def input_cash(self):  # 1-1. 현금결제
        self.cash = int(input("현금을 투입해주세요: "))
        self.card = 0
        print(f"현재 투입금액: {self.cash}")
        self.choose_product()

    def input_card(self):  # 1-2. 카드결제
        self.card = 1
        print("카드리더기에 카드를 대주세요.")
        self.choose_product()

    def choose_product(self):  # 결제 방식 선택 후 제품 고르기
        item_name = input("원하시는 제품의 제품명을 입력해주세요: ")
        result = list(
            filter(
                lambda product: item_name.lower() in product.item.lower(),
                self.product_list,
            )
        )

        if not result:
            print("제품을 찾을 수 없습니다.")
            return

        product = result[0]
        if product.stock <= 0:
            print("죄송합니다. 현재 제품의 재고가 존재하지 않습니다.")
            return

        self.howmany_product(product)

    def howmany_product(self, product):
        while True:
            try:
                item_count = int(
                    input(f" {product.item}의 원하시는 수량을 입력해주세요: ")
                )

                if item_count <= 0:
                    print("잘못 입력하셨습니다.")
                    continue
                if item_count > product.stock:
                    print(
                        f"선택하신 상품의 개수가 {product.stock} 개 남아있습니다. 주문 가능 수량 이하로 선택해 주세요."
                    )
                    continue
                for _ in range(item_count):
                    self.cart.append(product)
                print(
                    f"{product.item} {item_count} 개가 카트에 담겼습니다. added to cart."
                )
                break
            except ValueError:
                print("유효한 수량을 입력해 주세요.")

        self.want_more()

    def want_more(self):
        while True:
            print("1.더 고르기")
            print("2.결제하기")
            choice = input("Select: ")
            if choice == "1":
                self.choose_product()
            elif choice == "2":
                self.payment()
                break
            else:
                print("유효하지 않은 선택입니다.다시 입력해 주세요.")

    def add_money(self):
        a = int(input("현금을 투입해주세요: "))
        self.cash += a
        self.payment()

    def payment(self):
        total_price = sum([p.price for p in self.cart])
        print(f"총금액은 {total_price}입니다.")

        if self.card == 1:
            print("결제가 완료되었습니다.")

        else:
            change = self.cash - total_price
            if change < 0:
                print("결제금액이 부족합니다. 현금을 추가로 투입해주세요.")
                print(f"부족한 금액 : {-change}")
                self.add_money()
                return

            else:
                print(f"결제가 완료되었습니다. 거스름돈은 {change}입니다.")

        

        # Reduce stock
        for p in self.cart:
            p.stock -= 1
            self.sales_count[p.item] += 1

        self.total_sales += total_price

        # Reset
        self.cash = 0
        self.card = 0
        self.cart = []

        print("이용해 주셔서 감사합니다:)")
        exit()


    def howtouse(self):
        print("\n--- How to use this Vending Machine ---")
        print("1. 숫자 '1'을 입력해 결제 방식을 선택합니다.")
        print("2. 판매 중인 제품 목록을 확인하고 구매하고자 하는 제품명을 입력합니다.")
        print("3. 제품을 모두 선택하신 후 결제하기를 진행합니다.")

    def cs(self):
        print("\n--- Customer Service Center---")
        comment = input("문의사항 또는 불편사항을 입력해주세요:")
        self.sc.append(comment)

    def start(self):
        while True:
            print(
                "\n--- Customer Menu ---"
            )  # class에 따라 메뉴도 나누기 --> feedback : 결제 방식 선택(현금과 카드 복합결제가 가능할지)
            print("1.결제방식 선택")
            print("2.자판기 사용법")
            print("3.customer service")
            print("0. 종료")
            choice = input("Select: ")

            if choice == "1":
                self.howtopay()
            elif choice == "2":
                self.howtouse()
            elif choice == "3":
                self.cs()
            elif choice == "0":
                print("종료")
                break
            else:
                print("잘못된 접근입니다.")


if __name__ == "__main__":
    from vmManager import VMManager

    vmM = VMManager()
    vc = VMCustomer(vmM.product_list)
    vc.print_menu()
    vc.start()
