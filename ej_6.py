"""Write a program that creates a tuple with the names of the months of the year. Then, the
program will ask the user for a number. If the number is between 1 and the maximum length of
the tuple, it will show the corresponding month of the year. Otherwise, it will show an error
message and will ask for another number. The program will run until the user enters a 0."""

months = ('January','February','March','April','May','June','July','August','September','October','November','December')
num=input("Write your num")
while num > len(months):
  num=input("Write another num between 12 and 1")
if num==0 :
  print("end")
else:
  print(months[num])
