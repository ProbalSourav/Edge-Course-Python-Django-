class Person:
      #constructor
     def __init__(self,name,age) :
      self.name=name # Assign name
      self.age=age # Assign age
    
     # Method to display the person's info 
     def display_info(self):
       print(f"Name : {self.name}")
       print(f"Age : {self.age}")
       
     # Method to greet the person  
     def greet(self):
        print(f"Hello, {self.name}! Nice to meet you!")
        
     # Method to update the person's age
     def update_age(self, new_age):
        self.age = new_age
        print(f"{self.name}'s age has been updated to {self.age}")
   
        
# Creating an object of the class Person   
person1=Person("Alice",30)     
     
# Printing the name and age     
person1.display_info()     
     
# Greeting the person     
person1.greet()          
     
        
        