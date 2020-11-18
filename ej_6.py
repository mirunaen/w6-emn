A = []
B = [[],[]]
rows_A = int(input("Enter the number of rows of A and press enter: "))
column_A = int(input("Enter the number of columns of A and press enter:"))
#rows_B = int(input("Enter the number of rows of B and press enter:"))
#column_B = int(input("Enter the number of columns of B and press enter:"))
while len(A) < rows_A:
  for i in range(0,rows_A):
    A.append([])
    for j in range (0, column_A):
      n = int(input("Number: " ))
    A[j].append(n)