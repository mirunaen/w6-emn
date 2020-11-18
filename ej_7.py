"""Create a NxN matrix (represented as list of lists) where the first N - 1 columns have numbers
and the last column contains the result of adding the numbers in previous columns. Show the
matrix as follows:
10 + 9 + 3 = 22
4 + 8 + 7 = 19
1 + 9 + 7 = 17
2 + 8 + 8 = 18
"""

from random import randint

mat=[[0 for i in range(4)] for i in range(4)]

for i in mat:
  for n in range(len(i)):
    i[n]= randint(1,10)
  i[-1]=0
  i=[-1]=sum(i)

for i in mat:
  print(i[0],end="")
  for n in range(1,len(i)-1):
    print(" +",i[n],end="")
  print(" =",i[-1])