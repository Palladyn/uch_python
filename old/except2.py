import sys
f1="d:\\testq.txt"
while True:
    try:
        print("start try")
        my1 = open(f1, mode='r', encoding='ascii')
    except Exception:
        print("Inside except")
        print("Eror")
        print(sys.exc_info()[1])
        f1=input("Enter File name\n")
    else:
        print("else")
        print(my1.read())
        break




print("=====================================================")
print("\t \t\t\t\t End")