list1=[1,2,3,4,5,7]
list1[0]=list1[2]
print(list1[0],list1[2])
list1[2]=4
print(list1[0],list1[2])

#The value of list1[0] doesnt change because we say hey the first number will be the third one,okay,now we will change the thrid one to 4 but not the 1ª one.The same would happen if we reverse the order.

