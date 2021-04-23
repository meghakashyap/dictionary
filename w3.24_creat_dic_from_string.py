#1st way
string='w3resource'
count=1
result=dict.fromkeys(string,count)
print(result)

#2nd way
string='w3resource'
dic={}
i=1
for letter in string:
    dic[letter]=i
    i+=1
print(dic) 

# 3rd way
value="w3resources"
empty={}
for i in range(0,len(value)):
    count=1
    if value[i] in empty:
        count+=1
    empty[value[i]]=count
print(empty)

#create a dic 