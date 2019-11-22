def fact(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x*fact(x-1)


z=fact(10)
print(z)