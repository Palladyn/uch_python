def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1)+fib(x-2)


p=fib(10)

print(p)