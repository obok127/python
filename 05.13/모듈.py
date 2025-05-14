def add(x,y):
    return x+y

def sub(x,y):
    return x-y

class Person:
    def __init__(self, name=",", age=0):
        self.name = name
        self.age = age

    def print(self):
        print(f"name={self.name} age = {self.age}")

print( add(3,4) )
print( sub(3,4) )

p1 = Person("김도영", 30)
p1.print()
