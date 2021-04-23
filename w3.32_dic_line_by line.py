students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
for key in students:
    print(key)
    for value in students[key]:
        print(value ,":",students[key][value])
#print dictionary line by line