user=int(input("enter any num="))
dic= {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
if user in dic:
    del dic[user]
    print(dic)
else:
    print("doesnt exsist")
#delete if key and user same
