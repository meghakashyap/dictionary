employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
dic={}
for i in range(0,len(employees)):
    dic[employees[i]]=defaults
print(dic)
#intalize dic with default value