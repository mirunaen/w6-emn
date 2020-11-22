def count(list,x):
  counter=0
  for i in list:
    if i ==x:
      counter +=1
  return counter

def index(list,x):
  for i in range(len(list)):
    if list[i] == x:
      return index
    elif x not in list:
      return -1

def append(list,x):
  newList=list + [x]
  return newList

def find(list,x):
  if x in list:
    return True
  else:
    return False

def insert(list,x,index):
  x= [x]
  list=list[:index] + x + list[index-1:]
  return list

def remove(list,x):
  for i in range(len(list)):
    if list[i]==x:
      del list[i]
      return list

def removeAll(list,x):
  list1=[]
  for i in list:
    if i!= x:
      list2=[i]
      list1 +=list2
  return list1


def clear(list):
  list=[]
  return list

def pop(list):
  a=list[-1]
  del list[-1]
  return a

list1=[1,2,3,4,5,8]
print(count(list1,2))
print(index(list1,5))
print(append(list1,0))
print(find(list1,3))
print(insert(list1,0,2))
print(remove(list1,2))
print(removeAll(list1,2))
print(clear(list1))
print(pop(list1))
