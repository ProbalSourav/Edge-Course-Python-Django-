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
   
        
# Creating two objects of the class Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
     
# Updating the age of person1     
person1.update_age(32)     
     
# Printing the updated details of both objects
person1.display_info()
person2.display_info() 

       
     
        
        