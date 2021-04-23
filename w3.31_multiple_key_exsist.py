student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}
print(student.keys() >= {"name","class"})
print(student.keys() >= {'name', 'Alex'})
print(student.keys() >= {'roll_id', 'name'})

#checking the multiple key is exsist or not