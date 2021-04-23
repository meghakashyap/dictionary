word="MISSISSIPPI"
dic={}
i=0
while i<len(word):
    count=0
    j=0
    while j<len(word):
        if word[i]==word[j]:
            count+=1
        j+=1
        dic[word[i]]=count
    i+=1
print(dic)

#2nd way
for i in word:
    count=0
    for y in word:
        if [i]==[y]:
            count+=1
    dic[i]=count
print(dic)

#count occurance