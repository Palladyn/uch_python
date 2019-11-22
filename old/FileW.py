f1="d:\\test.txt"
f2="d:\\test3.txt"
key1="2"
key2="5"
my1=open(f1,mode='r',encoding='ascii')
my2=open(f2,mode='a',encoding='ascii')


for m in my1:
   if (key1 in m) or (key2 in m):
        my2.write(m)