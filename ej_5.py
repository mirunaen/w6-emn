import random 
maxim=5
print("Think about a num between 1 and",maxim)
list=[]
guess= False
fin=False
for i in range(1,maxim+1):
  list.append(i)
while guess ==False and fin ==False:
  n=random.ransint(1,maxim)
  if n in list:
    print(n)
    num=input("Is this your num?(y/n)")
    list.ramove(n)
    if num=="yes" or num="YES":
      guess=True
    else:
      tries=maxim - len(list)
      if tries == maxim:
        print("You´re lying!Your num doesnt exist or is not in the range")
        fin=True
if guess==True:
  print("Guessed it!")
  tries=maxim-len(list)
  print("In just",tries,"tries.")