dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for i in dic2:
    if i in dic1:
        dic2[i]+=dic1[i]
d={**dic1,**dic2,**dic3}
print(d)


#2nd Way
from collections import Counter
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
d = Counter(dic1) + Counter(dic2)+ Counter(dic3)
print(d)

#que 1 saral