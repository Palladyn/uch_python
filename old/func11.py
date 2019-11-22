import sys
def pozdr(name):
   print("pozdravl %s s dnem rozhdeniya"% name)
print("===================================================")

def summa(x,y):
    s=x+y
    return s


def factor(m):
    s=1
    for i in range (1,m+1):
        s=s*i
    return s




w=factor(5 )
print(w)
sys.stdin.readline()