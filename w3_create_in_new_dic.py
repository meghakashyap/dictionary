dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
#creat a new dictionary

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for result in (dic1,dic2,dic3):
    dic4.update(result)
print(dic4)
#2nd way to merge dic