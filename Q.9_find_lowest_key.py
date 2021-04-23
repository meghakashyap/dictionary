sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
min=sampleDict["Physics"]
for i in sampleDict:
    if sampleDict[i]<min:
        min=sampleDict[i]
        key=i
print(key)
#print the lowest key