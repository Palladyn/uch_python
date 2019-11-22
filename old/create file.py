file=open('d:\\test.txt')
x=file.read()
k=open('d:\\test2.txt','x')
k.write(x)
k.close()
file.close()
m=open('d:\\test1.txt')

print(m.read())
