my_dic={"a":1,"b":2,"c":3,"a":5}
dic={}
for key,value in my_dic.items():
    if value not in dic.keys():
        dic[key]=value
print(dic)
# #remove duplicate
