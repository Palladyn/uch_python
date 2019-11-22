import re
in_f="d:\\test.txt"
out_f="d:\\test2.txt"
my_in=open(in_f,mode='r',encoding='Latin-1')
res=open(out_f,mode='w',encoding='Latin-1')
tx=my_in.read()

key=r"[\w._-]+@[\w._-]+\.[\w.]+"

result=re.findall(key,tx)
for i in result:
    x=i+"\n"
    print(i)
    res.write(x)