"""A gymnast can receive a score between 1 and 10 from each judge; nothing lower, nothing
higher. All scores are integer values; there are no decimal scores from a single judge. There are
5 judges. Write a program that stores the possible scores a gymnast can get in a tuple
(randomly generated). Print out the following sentences using the values of the tuple:
Judge i gave the gymnast n points (or Judge i gave the gymnast 1 point)
The lowest score is x, and the highest score is y
Note: the max() function, returns the largest number in a given list or tuple. That is, given the
tuple t = (1,2,3) max(t) returns 3. On the other hand, the min(), returns the smallest
number in a given list or tuple. That is, given the tup"""

import random
list1=[]
for i in range (1,6):
  score=random.randint(1,10)
  list1.append(score)
tuple1=tuple(list1)
print("The judge 1  gave the gymnast",tuple1[0],"points")
print("The judge 2  gave the gymnast",tuple1[1],"points")
print("The judge 3  gave the gymnast",tuple1[2],"points")
print("The judge 4  gave the gymnast",tuple1[3],"points")
print("The judge 5  gave the gymnast",tuple1[4],"points")
