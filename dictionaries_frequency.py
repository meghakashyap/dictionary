list = [{"gfg" : 1, "is": 4, "best": 9},

             {"gfg" : 6, "is": 3, "best": 8},

             {"gfg": 1, "is" : 4, "best": 9},

             {"gfg": 1,"is": 1, "best" : 9}]
empty=[]             
for i in list:
    c=0
    dic=[]
    for j in list:
        if i == j :
            c+=1
    dic.append(i)
    dic.append(c)
    if dic not in empty:
        empty.append(dic)
print(empty)
#dictionaries frequency