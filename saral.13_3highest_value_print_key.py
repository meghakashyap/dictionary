my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
max=0
for dic in my_dict:
    c=0
    for x in my_dict:
        if my_dict[dic]>my_dict[x]:
            max=my_dict[dic]
            value=dic
            c+=1
        if c==3:
            print(dic, end=" ")
            # print(max)
            break
#3 highest key