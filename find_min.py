my_dic = {'x':500, 'y':5874, 'z': 560}
min=my_dic["x"]
for dic in my_dic:
    if my_dic[dic]<min:
        min=my_dic[dic]
print(min)