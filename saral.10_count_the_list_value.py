dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
c=0
f=0
for i in dict.values():
   for x in i:
      c+=1
print(c)
#count the value which is present in list