#vmData file
class VMData:
    def __init__(self, item="", price=0, stock=0, date=""): #문자열은 "",숫자는 0
        self.item = item
        self.price = price
        self.stock = stock
        self.date = date

    def print_customer(self):
        print(f"Item: {self.item}, Price: {self.price}, Expiry Date: {self.date}")

    
    def print_manager(self):
        print(f"Item: {self.item}, Price: {self.price}, Stock: {self.stock}, Expiry Date: {self.date}")

        