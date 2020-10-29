import time
import random

start=time.time()
list1=[]

#Method 1 
for i in range(100000):
  list1.append(random.randint(0,100))
end=time.time()
print(end-start)

start2=time.time()
list2=[]

#Method 2
counter=0
while counter < 100000:
  number = [random.randint(0,100)]
  list2 += number
  counter +=1
end2=time.time()
print(end2-start2)

start3=time.time()
list3=[]

#Method 3
counter = 0
while counter < 10000:
  number2=[random.randint(0,100)]
  list3=list3 + number2
  counter +=1
end3=time.time()
print(end3-start3)