f1="d:\\testq.txt"
try:
    print("start try")
    my1=open(f1,mode='r',encoding='ascii')

except Exception:
    print("Inside except")
    print("Eror")
else:
    print("else")
    print(my1.read())
finally:
    print("Fin")


print("=====================================================")
print("\t \t\t\t\t End")