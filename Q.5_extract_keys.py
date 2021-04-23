sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}
keys=["name","salary"]
dic={}
for i in keys:
    dic[i]=sampleDict[i]
print(dic)

#2nd way
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}
keys=["name","salary"]
newDict = {k: sampleDict[k] for k in keys}
print(newDict)

#extract keys and make new dict