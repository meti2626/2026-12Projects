class Restaurant:
  def __init__(self , restaurant_name,  cuisine_type):
        self.RN = restaurant_name
        self.CT = cuisine_type
        self.number_served = 0

  def describe_restaurant(self):
         print(f"restaurant name and cuisine {self.RN} &{self.CT}")     
  def  open_restaurant(self):
       print(f"restaurant is open")      

  def set_number_served(self , number):
       self.number_served = number

  def increment_number_served(self,increment):
        self.number_served += increment 
        
restaurant = Restaurant("hilton","cake")


# My_restaurant = Restaurant("sharatan" , "stake")
# your_restaurant = Restaurant("trump" , "fish")

restaurant.describe_restaurant()
restaurant.set_number_served(25)
restaurant.increment_number_served(100)
print(restaurant.number_served)
# My_restaurant.describe_restaurant()
# your_restaurant.describe_restaurant()
class User:
     def __init__(self, FN , LN):
        self.fn = FN
        self.ln = LN
     def describe_user(self):
          print(f"My name is {self.fn} {self.ln}")


     def greet_user(self):
          print(f"good to see you {self.ln}")  

          
first_user = User ("kate" ,"John")
second_user = User("andrew" , "colvet")


first_user.describe_user()
first_user.greet_user()
second_user.describe_user()
second_user.greet_user()


