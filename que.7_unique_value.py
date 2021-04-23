sample=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
] 
dic={}
dic1=[]
for i in range(0,len(sample)):
     for value in sample[i]:
          dic=(sample[i][value])
     if dic not in dic1:
          dic1.append(dic)
print(dic1)
#print unique 