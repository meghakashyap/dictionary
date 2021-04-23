keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dic={}
for x in keys:
    for y in values:
        dic[x]=y
        values.remove(y)  
        break
print(dic)
#merge two list and make a dictionary