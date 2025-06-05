def recursive_call(n):
    if n > 10:  # 함수의 종료조건이 중요하다
        return
    print(n)
    recursive_call(n + 1)


recursive_call(1)


def recursive_call2(n):
    if n < 1:
        return
    print(n)
    recursive_call2(n - 1)


recursive_call2(10)


def fibonacci(n):
    if n==1 or n==2:
        return 1
    return fibonacci(n-2) +fibonacci(n-1)

print("3번째요소", fibonacci(3) )
print("6번째요소", fibonacci(6) )



def sumAll(n):
    if n==0:
        return 0
    return n + sumAll(n-1)

print(sumAll(10))

def mysum(n):
    if n <=1:
        return 1
    return mysum(n-1) + n

print(mysum(10))

