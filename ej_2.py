def combine(list1,list2):
  combination=[]
  for i in list1:
    if i not in list2:
      combination.append(i)
  for i in list2:
    combination.append(i)
  
  return combination

list1=[1,2,3,4,5,6]
list2=[3,4,5,7,8,9]

print(combine(list1,list2))