from urllib import request,parse
import sys
silka= "https://www.google.com/search?"
val={'q':'Paranormal news'}
heder={}
heder['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'


try:
    data=parse.urlencode(val)
    print(data)
    silka=silka+data
    rec=request.Request(silka,headers=heder)
    otv=request.urlopen(rec)
    otv=otv.readlines()
    for k in otv:
        print(k)

except Exception:
    print("Error")
    print(sys.exc_info()[1 ])


