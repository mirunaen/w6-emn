"""Write a program that asks the user to enter a sentence. Then, it introduces each character of
the sentence in a tuple, ignoring the repeated characters. The characters introduced in the
tuple should be capitalized (you can use the upper() method of strings). Finally, it prints the
tuple. """

sentence=input("Write a sentence")
sentence=sentence.upper()
tuple1=tuple(sentence)
list=[]
for i in tuple1:
  if i not in list:
    list.append(i)
tuple2=tuple(list)
print(tuple2)

