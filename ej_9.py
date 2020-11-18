from random import randint

m = [[0 for i in range (3)] for i in range (3)]

tmp = 0

for i in m:
  for n in range (Len(i)):
    rep = True
    while rep:
      rep=False
      tmp = randint(1, 25) # put the random value into temporary variable
      for k in m: # iterate through each nested list
        if tmp in k:
          rep = True
        if not rep: # if the value is not in any of three lists, we can add it to the matrix
          1[n]= tmp

for i in m:
  for n in i:
    print(n, end="")
  print ()
print()

tmp = 1
ms =[0 for i in range (3)] for i in range(3)]

for i in ms:
  for n in range (Len(1)):
    rep = True
    while rep:
      for k in m:
        if tmp in k:
          i[n] = tmp
          rep = False

        tmp += 1

for i in ms:
  for n in 1:
    print(n, end="")
  print()