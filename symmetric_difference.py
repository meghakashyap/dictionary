dict1 = {"Gfg" : 4, "is" : 3, "best": 7, "for": 3, "geek" : 4}
dict2 = {"Gfg" : 4, "is" : 3, "good" : 7, "for" : 3, "all": 4}
dic={}
for key in dict1:
    for key1 in dict2:
        if key not in dict2:
            dic[key]=dict1[key]
        if key1 not in dict1:
            dic[key1]=dict2[key1]
print(dic)
#print symmetric difference of dic

