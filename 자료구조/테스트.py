def sumAll(n):
    if n == 0:
        return 0
    return n + sumAll(n - 1)


print(sumAll(10))
