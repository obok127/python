class MyQueue:
    def __init__(self, size=10):
        if size<10: #최소 10이상
            size = 10
        self.size = size
        self.queue = [None] * self.size
        print(self.queue)
        self.front = 0
        self.rear = 0

    def put(self, data):
        """
        rear 하나 증가시킨 후에  % self.size로 나머지를 구하고 
        그 위치에 데이터를 넣기
        """
        if self.isFull():
            print("queue is full")
            return
        self.rear = (self.rear+1)%self.size
        self.queue[self.rear]=data

    
    def isEmpty(self):
        if self.rear == self.front:
            return True
        return False

    def isFull(self):
        if (self.rear+1)%self.size == self.front: #self.rear+1%self.size 가 한바퀴 돌게 만드는 코드)
            return True
        return False

    def get(self):
        """
        front 증가시켜서 그 위치값 반환하기
        """
        if self.isEmpty():
            print("queue is Empty")
            return
        self.front = (self.front+1)%self.size
        return self.queue[self.front]

    def peek(self):  #self.front를 바꾸지 않으면서 그 다음 칸에 있는 값을 살짝 들여다만 보는 것
        """
        front를 증가시켜서 그 위치값을 반환하는데
        front 자체는 바꾸면 안됨
        """
        if self.isEmpty():
            print("queue is Empty")
            return
        temp = (self.front+1)%self.size
        return self.queue[temp]

class BankNumber:
    def __init__(self):
        self.number=0 #번호가 0
        self.cnt=0 #현재 대기 인원 수
        self.queue = MyQueue(500) #큐의 크기가 500

    def menuCustomer(self):
        self.number += 1
        self.cnt +=1
        self.queue.put(self.number)
        print(f"대기인원 {self.cnt}")
        print(f"고객님 번호는 {self.number}입니다.") #queue는 가져오는 쪽에서 써야 한다.

    def menuBanker(self):
        #큐에서 번호 하나를 꺼낸다
        if self.queue.isEmpty():
            return
        self.number = self.queue.get()
        print(f"{self.number} 고객님 창구 앞으로 와주세요.")
        self.cnt -=1
        print(f"대기인원 {self.cnt}")
        
    def main(self):
        while True:
            sel = input("1.고객 2.은행원 3.종료")
            if sel=="1":
                self.menuCustomer()
            elif sel=="2":
                self.menuBanker()
            elif sel=="3":
                return
            else:
                print("쫌")
    

if __name__ == "__main__":
    bm = BankNumber()
    bm.main()

