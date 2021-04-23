#1st way
a={"a":100,"b":200,"c":300}
b={"a":300,"b":200,"d":400}
c={}
for x in a:
    for y in b:
        if x == y:
            c[x] = a[x]+b[y]
            break
    else:
        c[x] = a[x]
        c[y] = b[y]
print(c)

#2nd way
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)
#adding same value

#3rd way
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for i in d2:
    if i in d1:
        d2[i]+=d1[i]
dic={**d1,**d2}
print(dic)

