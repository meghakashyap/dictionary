dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dic = {**dict1, **dict2}
print(dic)

#2nd way
dic_e={}
for i in dict1:
    dic_e=dict1,dict2
print(dic_e)

#merge two dict