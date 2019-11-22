import sys
def ves ():
    print('ukajite svoy ves')
    v=int(sys.stdin.readline())

    print('ukajite koef')
    k = float(sys.stdin.readline())

    print('ukajite goda')
    y = int(sys.stdin.readline())
    for i in range (0,y+1):
        mv=v*k+i*k
        print ("%s mi ves : %s" %  (i,mv))