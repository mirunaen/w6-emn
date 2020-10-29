list1=[1,2,3,4,5,7]
list1[0]=list1[2]
print(list1[0],list1[2])
list1[2]=4
print(list1[0],list1[2])

#The value of list1[0] doesnt change because we say hey the first number will be the third one,okay,now we will change the thrid one to 4 but not the 1ª one.The same would happen if we reverse the order.

"""import random

rigth=False
while not rigth:
  num=int(input("Enter a num:"))
  if num > 5:
    rigth=True

result=0
previous=0
for i in range(1,num+1):
  total=random.randint(1,10)
  print("Num generated",total)
  if total > previous:
    print("Bigger than previous.Add it",result)
    result=total + previous
    
  else:
    print("Not bigger than the previous one,I will substract it")
    result=total-previous
previous=total
print("The current value is",num)
    


print(total)"""
"""import random 
list1=[]
list2=[]

for i in range(1,100):
  n=random.randint(0,100)
  u=random.randint(0,100)
  list1.append(n)
  list2.append(u)


num=int(input("Enter num between 1 and 100:"))
if num not in range(1,100):
  num=int(input("Enter num between 1 and 100:"))
else:
  if num in range(1,100):
   position1=list1.index(num)
   position2=list2.index(num)
   if num=position1:

  else:
    print(num,"not in the list")

  list1=[1,2,3]
  for i in list1:
    print(i)


  """

"""list1=[1,2,3]
list2=[4,5,6]
list1.append(88)
list2.extend(list1)
print(list1)
print(list2)"""