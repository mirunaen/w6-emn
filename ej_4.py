def fibonnaci(num):
  num1=0
  num2=1
  series=[0]
  for i in range(num):
    num1=num2
    num2=series[-1]
    series.append(num1 + num2)
  return series

num=int(input("Enter num of elements to perform fibonacci sequence(positive int):"))
print(fibonnaci(num))