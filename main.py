import random

maria = {"name": "Maria","homework":[],"weekAssignments":[]}
pedro = {"name": "Maria","homework":[],"weekAssignments":[]}
miguel = {"name": "Maria","homework":[],"weekAssignments":[]}

print(maria,pedro,miguel)

# Marks for in range(1,11):
for i in range(1, 11):
  nota=random.randint(0, 10) 
  maria["homework"].append(nota)

for i in range(1, 11):
  nota=random.randint(0, 10) 
  pedro["homework"].append(nota)

for i in range(1, 11):
  nota=random.randint(0, 10) 
  miguel["homework"].append(nota)

#Week assignments
for i in range(1, 11):
  nota2=random.randint(0, 10) 
  maria["weekAssignments"].append(nota2)

for i in range(1, 11):
  nota2=random.randint(0, 10) 
  pedro["weekAssignments"].append(nota2)

for i in range(1, 11):
  nota2=random.randint(0, 10) 
  miguel["weekAssignments"].append(nota2)


maria["test"]=random.randint(0,10)
pedro["test"]=random.randint(0,10)
miguel["test"]=random.randint(0,10)