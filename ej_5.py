from random import randint
def ask_for_num():
  usr_input=0
  while usr_input < 1 or usr_input >10:
    usr_input=int(input("Enter a num between 1 and 10:"))
    return usr_input

def generate_rand_list(size):
  return [randint(1,10) for i in range(size)]

def list_min(list1):
  list_cp=list1.copy()
  list_cp.sort()
  return list_cp[0]

list_size=ask_for_num()
rand_list=generate_rand_list(list_size)
print(rand_list)
print(list_min(rand_list))