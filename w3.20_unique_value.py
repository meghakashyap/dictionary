demo=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
empty=[]
test=[]
for d in range(0,len(demo)):
    for key1,value1 in demo[d].items():
        if demo[d][key1]!=empty:
               empty=(demo[d][key1])
        if empty not in test:
            test.append(empty)
print(test)
# print unique value

