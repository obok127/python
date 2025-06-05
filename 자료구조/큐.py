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
            return None
        self.front = (self.front+1)%self.size
        return self.queue[self.front]

    def peek(self):  #self.front를 바꾸지 않으면서 그 다음 칸에 있는 값을 살짝 들여다만 보는 것
        """
        front를 증가시켜서 그 위치값을 반환하는데
        front 자체는 바꾸면 안됨
        """
        if self.isEmpty():
            print("queue is Empty")
            return None
        temp = (self.front+1)%self.size
        return self.queue[temp]

if __name__ == "__main__":
    q = MyQueue()
    q.put('A')
    q.put('B')
    q.put('C')
    q.put('D')
    q.put('E')
    q.put('F')
    q.put('G')
    q.put('H')
    q.put('I')
    q.put('J')

    print(q.queue)
    print(q.peek())
    print(q.queue)

    while not q.isEmpty():
        print(q.get()) #배열의 인덱스 값을 돌린다고 해서 환형 큐라고 함.




