import random
list=[]

length=int(input("Enter the length: "))
total=0
while length <=0:
  length=int(input("The length must be grater than o,try again:"))
while len(list) < length:
  element=random.uniform(1,50)
  list.append(element)
print(list)
for num in list:
  total +=num//1
  print("Total",total)