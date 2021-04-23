sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}
for i in sampleDict:
    if sampleDict[i]["name"]=="Brad":
        sampleDict["emp3"]["salary"]=8500
        print(sampleDict)
#change the salary