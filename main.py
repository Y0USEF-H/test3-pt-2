# I tried 
#idk why its not working :/

def function_one(): #Define function
  user_input=input("whats your string") #prompt and input
  A=[]
  B=[]
  for element in user_input: #for looop
    if element.isdigit(): #see if its a digit 
      A.append(element) 
    else:           #use append to add the the end of list
      B.append(element) 
  return A
    


def function_two(list_of_numbers): #Define function
  list_one = list_of_numbers[1::2] 
  list_two = list_of_numbers[0::2]
  sorted_list_one = sorted(list_one, reverse=True) #sort list_one in reverse
  i = 1 #initialize a variabl to keep track of index that we will insert into I and variable to track the index that we will be using to insert into the Z list
  z = 0
#Loop through the list, inserting an element from the Reversed list every other element of non-reversed list
  while i < len(list_two):
    list_two.insert(i, sorted_list_one[z])
    i += 2
    z += 1
  return list_two