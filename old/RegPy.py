import re
my= " Petro zxczxbcznb 1977, Kolyan -1988: Olga 1987, pmskt@ms.com "\
    "sgdfhajsdas@int.com, Polina xxxxxxxx 1996,dmsdmfmds@mail.ru"\
    "dsfdsfs@ya.ru, dima@fwt.com.ua, hello world, Miner #18 1991"\
    "Viliam 1967, Irisha , 2001, aneta@ms.com, dildo@mail.ru" \
    "ohin@mail.ru,hhhiom@kin.ru, litor@gov.ua"\
"""
\d = Любая цыфра
\D = любой символ но не цыфра
\w =любой алфавитній симовл [A-Z a-z]
\W= любой но не алфавит
\s = пробелы
\S =  что угодно но не пробел

[0-9] поиск цыфр указанного диапазона
[A-Z] поиск Букв больших
[a-z] поиск малых букв

"""

tim=r"\d+ "
res=re.findall(tim,my)

print(res)