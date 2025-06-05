# 스택을 사용해서 문자열 뒤집기
# s2 = MyStack(30)


class MyStack:
    def __init__(self, size=30):
        if size < 30:
            self.size = 30
        else:
            self.size = size
        self.stack = [0] * self.size  # 리스트를 크기만큼 0으로 초기화
        self.top = -1
        self.size = size

    # push 함수
    # isFull상태가 아니면 top 증가시키고 그 안에 값 넣기
    def isFull(self):
        if self.size - 1 == self.top:
            return True
        return False

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def push(self, data):
        if self.isFull():
            return
        self.top += 1
        self.stack[self.top] = data

    def print(self):
        i = 0
        while i <= self.top:
            print(self.stack[i], end=" ")
            i += 1
        print()

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[self.top]

    def pop(self):
        if not self.isEmpty():
            value = self.stack[self.top]
            self.top -= 1
            return value
        return


def reverse(arr):
    s = MyStack(len(arr))
    for i in arr:
        s.push(i)

    result = ""
    while not s.isEmpty():
        result += s.pop()
    return result


print(reverse("korea"))
