class MyStack:
    def __init__(self,size = 10):
        if size < 10:
            self.size = 10  #최소 크기를 10으로 하자
        else:
            self.size = size
        self.stack=[]
        for i in range(0,self.size):
            self.stack.append(0)
        self.top = -1
        self.size = size

    #push 함수
    #isFull상태가 아니면 top 증가시키고 그 안에 값 넣기
    def isFull(self):
        if self.size-1 == self.top:
            return True
        return False

    #pull 함수
    def isEmpty(self):
        if self.top == -1:
            return True
        return False

#스택 클래스에서 스택의 상태를 확인하고, 데이터를 넣고 빼

    def push(self, data):
        if self.isFull():
            return
        self.top += 1
        self.stack[self.top] = data
    
    def print(self):
        i = 0
        while i <= self.top:
             print( self.stack[i],end=" ")
             i+=1
        print()

    def peek(self):
        if self.isEmpty():
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item
    
    def pop(self):
        if not self.isEmpty():
            value = self.stack[self.top]
            self.top -= 1
            return value
        return


s1 = MyStack()
s1.push('A')
s1.push('B')
s1.push('C')
s1.push('D')
s1.push('E')
s1.push('F')
s1.push('G')
s1.push('H')
s1.push('I')
s1.push('J')
s1.push('K') # 스택 full상태라서 K가 들어가지 않음
s1.print()
print("-------------------")
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())




