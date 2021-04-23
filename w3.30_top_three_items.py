a={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max=0
for key in a:
    count=0
    for key1 in a:
        if a[key]>=a[key1]:
            max=a[key]
            value =key
            count+=1
        if count==3:
            print(value,max)
            break
#find 3 largest item