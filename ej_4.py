import random

maria = {"name": "Maria","homework":[],"weekAssignments":[]}
pedro = {"name": "Maria","homework":[],"weekAssignments":[]}
miguel = {"name": "Maria","homework":[],"weekAssignments":[]}

print(maria,pedro,miguel)

# Marks for in range(1,11):
for i in range(1, 11):
  mark=random.randint(0, 10) 
  maria["homework"].append(mark)

for i in range(1, 11):
  mark=random.randint(0, 10) 
  pedro["homework"].append(mark)

for i in range(1, 11):
  mark=random.randint(0, 10) 
  miguel["homework"].append(mark)

#Week assignments
for i in range(1, 11):
  mark2=random.randint(0, 10) 
  maria["weekAssignments"].append(mark2)

for i in range(1, 11):
  mark2=random.randint(0, 10) 
  pedro["weekAssignments"].append(mark2)

for i in range(1, 11):
  mark2=random.randint(0, 10) 
  miguel["weekAssignments"].append(mark2)


maria["test"]=random.randint(0,10)
pedro["test"]=random.randint(0,10)
miguel["test"]=random.randint(0,10)

students = [maria, pedro, miguel] 

for i in students: 
  sum = 0 
  for j in i['homework'][0]: 
    sum+=j 
  med = sum/10 
  i['homework'].append(med) 
  sum = 0 
  for j in i['weekAssignments'][0]: 
    sum+=j 
med = sum/10 
i['weekAssignments'].append(med) 

# Final mark

maria['mark'] = maria['homework'][1] * 0.1 + maria['weekAssignments'][1] * 0.3 + maria

pedro['mark'] = pedro['homework'][1] * 0.1 + pedro['weekAssignments'][1] * 0.3 + pedro
miguel['mark'] = miguel['homework'][1] * 0.1 + miguel['weekAssignments'][1] * 0.3 + miguel

maria['literalMark'] = None 
pedro['literalMark'] = None 
miguel['literalMark'] = None  

for i in students: 
  if i['mark'] >= 9: 
    i['literalMark'] = 'A' 
  elif i['mark'] >= 8 and i['mark'] < 9: 
    i['literalMark'] = 'B' 
  elif i['mark'] >= 7 and i['mark'] < 8: 
    i['literalMark'] = 'C' 
  elif i['mark'] >= 6 and i['mark'] < 7: 
    i['literalMark'] = 'D' 
  elif i['mark'] >= 5 and i['mark'] < 6: 
    i['literalMark'] = 'E' 
  else: 
    i['literalMark'] = 'F' 

# Result

for j in i: 
  print(j, ":", i[j]) 


