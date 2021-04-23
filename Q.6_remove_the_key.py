sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}
keysToRemove = ["name", "salary"]
j=0
for i in keysToRemove :
    del sampleDict[keysToRemove[j]]
    j+=1
print(sampleDict)

#remove the key