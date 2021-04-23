dic = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
for i in dic:
    for j in dic:
        if dic[i]>dic[j]:
            tem=dic[i]
            dic[i]=dic[j]
            dic[j]=tem
print(dic)
#descending the dic value