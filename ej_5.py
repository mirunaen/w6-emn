months = {'January': 31,
'Febr': None,
'March': 31,
'April': 30,
'May': 31,
'June':30,
'July':31,
'August': 31,
'September': 30,
'Octubre': 31,
'Noviembre': 30,
'Diciembre' : 31}
date = {'day': int(input("Write a day: ")) ,
'month' : input("Month: ") ,
'year': int(input("Year: ")),
'bisiest' : ''}
# year bisiest
if date['year']%4==0:
  if date['year']%100==0:
    if date['year']%400==0:
      date['bisiest'] = True
    else:
      date['bisiest'] = False
    else:
      date['bisiest'] = True
    else:
      date['bisiest'] = False
# Febrary
if date['bisiest'] == False:
  month['Febrero'] = 28
else:
  month['Febrero'] = 29
# Correct day
for i in month:
  while date['dia'] > month[i]:
    date['dia'] = int(input("Escribe un día: "))
for j in month:
  while date['mes'] not in month:
    date['mes'] = input("Escribe el mes (con la primera letra mayúscula): ")
#  date
if date['bisiest'] == True:
  print(date['dia'], 'de', date['mes'], 'de', date['year'], ', year bisiest.')
else:
  print(date['dia'], 'de', date['mes'], 'de', date['year'], ', year no bisiest.')