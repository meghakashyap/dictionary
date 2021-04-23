list = [7, 6, 3, 7, 8, 3, 6, 7, 8]
# Output: {8: [4, 8], 3: [2, 5], 6: [1, 6], 7: [0, 3,7]}
i=0
dic={}
empty2=[]
while i<len(list):
    index=0
    j=0
    s=[]
    empty1=[]
    while j<len(list):
        if list[i]==list[j]:
            empty1.append(j)
        j+=1
    empty2.append(list[i])     
    dic[empty2[i]]=empty1
    i+=1
print(dic)
#list occurance and indexing make a dictioanry
