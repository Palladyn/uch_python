unit={
    'pos_x'  :   100,
    'pos_y'  :   65,
    'color'  :   'sinii',
    'zhizn'  :   1000,
    'name'   :   'Painkiller',
    'snaryga':  ['shit','mech'],
    'klass'  :  ['varvar','ritsar']
}

vrags=[]
for x in range(0,10):
    vrags.append(unit.copy())
p=0
for i in vrags:
    p=p+1
    print(p)
    print (i)
    print("=================================================================================================================================================")

vrags[5]['zhizn']=300

print(vrags[5])
print("=================================================================================================================================================")

vrags[7]['name']="LOL"
vrags[7]['pos_x']+=10
print(vrags)
print("=================================================================================================================================================")