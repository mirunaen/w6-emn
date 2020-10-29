import random 
list1=[]

for i in range(1,21):
  n=random.randint(0,9)
  list1.append(n)

num=int(input("Enter num between 1 and 9:"))
if num not in range(1,9):
  num=int(input("Enter num between 1 and 9:"))
else:
  if num in range(1,9):
   position=list1.index(num)
   print(num,"is on the list.In the position",position)
  else:
    print(num,"not in the list")
  
