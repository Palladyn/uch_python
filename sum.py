def sum (x):
   if x==0:
       return o
   elif x==1:
       return 1
   else:
       return x+sum(x-1)

z=sum(30)
print(z)