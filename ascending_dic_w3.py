dic = {"A": 2, "B": 4, "C": 3, "D": 1, "E": 0}
for i in dic:
    for j in dic:
        if dic[i]<dic[j]:
            tem=dic[i]
            dic[i]=dic[j]
            dic[j]=tem
print(dic)
#ascending the dic value