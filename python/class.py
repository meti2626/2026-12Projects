# class Dog:

#   def __init__(self,name,age):
#    self.name = name 
#    self.age = age 

#   def sit(self):
     
#      print(f"{self.name} is now sitting.")


#   def roll_over(self):
#    print(f"{self.name} rolled over!")


# my_dog = Dog('Willie',6)
# your_dog = Dog("Lucy" , 3)


# # calling attrinbutes
# print(f"My dogs name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()

# print(f"your dogs name is {your_dog.name}.")
# print(f"your dog is {your_dog.age} years old.")


# #calling methodes


# your_dog.roll_over()

#car class

class Car:
  def __init__(self, make, model, year):
     self.make = make
     self.model = model
     self.year = year
     self.odometer_reading = 0
     
# when a methode s called by specific instance or object use self
  def get_descriptive_name(self):

     long_name =f"{self.year} {self.make} {self.model} "  
     return long_name.title()
  
  def update_odometer(self, mileage):
     self.odometer_reading = mileage
  

  def increment_odometer(self, miles):
       self.odometer_reading += miles


  def read_odometer(self):
     print(f"This car has {self.odometer_reading} miles on it.")

# my_new_car = Car('audi', 'a4', 2019)

# # my_new_car.update_oderometer(23)

# my_new_car.increment_oderomerter(100)

# print(my_new_car.get_descriptive_name())

# my_new_car.read_odometer()


my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())


my_used_car.update_odometer(23_500)
my_used_car.read_odometer()


my_used_car.increment_odometer(100)
my_used_car.read_odometer()



class ElectricCar(Car):


   def __init__(self, make, model, year):
      super().__init__(make, model, year)
      self.battery_size= 75
   

   def describe_battery(self):
      print(f"This car has a {self.battery_size}-KWH battery")


my_tesla = ElectricCar('tesla' , 'model' , 2019)
print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(34)
my_tesla.describe_battery()



