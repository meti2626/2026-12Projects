class Dog:

  def __init__(self,name,age):
   self.name = name 
   self.age = age 

  def sit(self):
     
     print(f"{self.name} is now sitting.")


  def roll_over(self):
   print(f"{self.name} rolled over!")


my_dog = Dog('Willie',6)
your_dog = Dog("Lucy" , 3)


# calling attrinbutes
print(f"My dogs name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"your dogs name is {your_dog.name}.")
print(f"your dog is {your_dog.age} years old.")


#calling methodes


your_dog.roll_over()

