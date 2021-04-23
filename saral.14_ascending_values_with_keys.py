dict1 = {"Apple": 9, "Banana": 32, "Cat": 24}
sorted_values = sorted(dict1.values()) # Sort the values
sorted_dict = {}
for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break
print(sorted_dict)


#2nd way
dict1 = {"Apple": 9, "Banana": 32, "Cat": 24}
key_list=[]
value_list=[]
for i in dict1:
    key_list.append(i)
    value_list.append(dict1[i])
for key in range(0,len(value_list)):
    for value in range(0,len(value_list)):
        if value_list[key]<value_list[value]:
            value_list[key],value_list[value]=value_list[value],value_list[key]
            key_list[key],key_list[value]=key_list[value],key_list[key]
des={}
for index in range(0,len(key_list)):
    des[key_list[index]]=value_list[index]
print(des)
#asscending the key and value of dic



