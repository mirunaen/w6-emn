"""Write a program that asks the user to enter a sentence. Then, it will introduce each character of
the sentence in a tuple, ignoring the spaces. Finally, it will print the tuple. For instance:
Write a sentence: Hi, how are you?
(’H’, ’i’, ’,’, ’h’, ’o’, ’w’, ’a’, ’r’, ’e’, ’y’, ’o’, ’u’, ’?’)"""

sentence=input("Write a sentence")
tuple1=tuple(sentence)
list=[]
for i in tuple1:
  if i !=" ":
    list.append(i)
tuple2=tuple(list)
print(tuple2)

