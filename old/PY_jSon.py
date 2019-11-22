import json

f="d:\\hero.txt"
my=open(f,mode='w',encoding='Latin-1')
gamer={
    'name'  :   'ishak',
    'score' :   345,
    'pos_x' :   10,
    'pos_y' :   45,

}
hero={
    'name'  :   'Elen',
    'score' :   217,
    'pos_x' :   10,
    'pos_y' :   45,
}
units=[]
units.append(gamer)
units.append(hero)

json.dump(units,my)
my.close()


my=open(f,mode='r',encoding='Latin-1')
my1=json.load(my)


print(my1)

print('===================================================================================================')

print(units)