dict = {"gfg" : [5, 3, 6, 3], "is" : [1, 7, 5, 3], "best" : [9, 1, 3, 5]}
# Output : {‘gfg’: 2, ‘is’: 1, ‘best’: 0}
max=0
c=0
dic={}
for key in dict:
    for index in range(0,len(dict[key])):
        if dict[key][index]>max:
            max=dict[key][index]
            value=index
            c+=1
    dic[key]=value
print(dic)
# #maximum element index

