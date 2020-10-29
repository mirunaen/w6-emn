import random
a = []
for i in range(0,22):
  n=random.randint(0,100)
  a.append(n)
b=a
a[10] = 12
print(a[10])
print(b[10])
print(a)
print(b)

#Yes,because they become the same list when we say a=b.
