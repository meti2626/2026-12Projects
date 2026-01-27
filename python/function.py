#def greet_user(usename): # parameter accepts the argument from the function call
  #print(f"hello!{usename.title()}")

#greet_user('jesse')  # jeese is an argument - passed from function call to function
#greet_user('sarah')  

# def get_formatted_name(first_name,last_name,middle_name=""):
#   full_name = f"{first_name} {middle_name} {last_name}"
#   return full_name.title()


# musician = get_formatted_name('jimi' , 'hendrix')
# print(musician)


#Returning a dictionary



# def build_person(first_name, last_name , age = None):
#   person = {'first':first_name , 'last':last_name ,'age':age}
 
#   if age:
#     person['age'] = age
#   return person  

# musician = build_person('jimi' , 'hendrix' , 27)
# print(musician)






#--------Using a Function with a while Loop------------#

# def get_formatted_name(first_name, last_name):

#  full_name = f"{first_name} {last_name}"
#  return full_name.title()



  # This is an infinite loop

# while True:
#    print("\nPlease tell me your name:")
#    print("(enter 'q' at any time to quit)")


#    f_name = input("First nam: ")
#    if f_name == 'q':
#         break
#    l_name = input("Last name : ")
#    if l_name == 'q':
#        break
   
#    formatted_name = get_formatted_name(f_name , l_name)
#    print(f"\nHello, {formatted_name}")




#------Passing A loop-----#

# def greet_users(names):

#    for name in names:
#       msg = f"Hello, {name.title()}"
#       print(msg)

# usernames = ['hannah','ty','margot']

# greet_users(usernames)

#---- Modifying a List in a function



# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# print("\nThe following models have been printed:")   

# for completed_model in  completed_models:
#     print(completed_model)


# def print_models(unprinted_designs, completed_models):
   
#    while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# def show_completed_models(completed_models):

#   print("\nThe following models have been printed:")
#   for completed_model in completed_models:
#      print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = [] 


# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)



#---PASSING AN ARBITRARY NUMBER OF ARGUMENTS----#




def make_pizza(*toppings,size):
   print(f"\nMaking a {size}-inch pizza with the following toppings:") 
   for topping in toppings:
    print(f"-{topping}")


make_pizza('pepperoni','margatita', 12 )
make_pizza(16, 'mushrooms','green peppers','extra cheese')