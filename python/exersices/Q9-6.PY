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
        self.login_attempts = 1

     def describe_user(self):
          print(f"My name is {self.fn} {self.ln}")

     def greet_user(self):
          print(f"good to see you {self.ln}")  

     def  reset_login_attempts(self):
             self.login_attempts = 0
     
     def  increment_login_attempts(self):
         self.login_attempts +=1 
     
    
          
first_user = User ("kate" ,"John")
second_user = User("andrew" , "colvet")

# print(first_user.login_attempts)
# first_user.reset_login_attempts()
# first_user.increment_login_attempts()
# first_user.increment_login_attempts()

# print(first_user.login_attempts)
# first_user.describe_user()
# first_user.greet_user()
# second_user.describe_user()
# second_user.greet_user()


class  IceCreamStand(Restaurant) :

  def __init__(self, restaurant_name, cuisine_type, *flavors):
       super().__init__(restaurant_name, cuisine_type)
       self.flavor =  flavors

  def  showFlavors(self):
    print( self.flavor)
       

Icecreamstand = IceCreamStand("chickflea" , "chicken", "chocolate" , "vanilla" , "sprinkles") 

#Icecreamstand.showFlavors()

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, FN, LN):
        super().__init__(FN, LN)
        self.privileges = Privileges()

# Create an instance of Admin and use the method to show its privileges
admin1 = Admin("Keith", "Alehandro")
admin1.privileges.privileges = ["can add post", "can delete post", "can ban user"]
admin1.privileges.show_privileges()
