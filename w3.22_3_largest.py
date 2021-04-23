my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20} 
max=0
for i in my_dict:
    c=0
    for y in my_dict:
        if my_dict[i]>my_dict[y]:
            max=my_dict[i]
            value=i
            c+=1
        if c==3:
            print(max)
            break
#3 highest value with key

    
