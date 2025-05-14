# 자판기 -> 객체지향
#VMData class file
class VMData:
    def __init__(self, item, price, stock, date):
        self.item = item
        self.price = price
        self.stock = stock
        self.date = date
        self.process()

    def process(self):
        self.change = self.price - (self.cash + self.card)
        if self.price > self.cash + self.card:
            self.statement = "Please insert more money"
        elif self.price == self.cash + self.card:
            self.statement = "You've inserted enough!"
        else:
            self.statement = "Here is your change:)"

    def print(self):
        print(f"cash:{self.cash}", end="\t")
        print(f"card:{self.card}", end="\t")
        print(f"total_price:{self.price}", end="\t")
        print(f"{self.statement}", end="\t")
        print(f"{self.change}")


if __name__ == "__main__":
    vm = VMData()
    vm.print()
