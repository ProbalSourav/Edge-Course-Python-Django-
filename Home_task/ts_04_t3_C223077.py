class Car:
  
   def __init__(self,model,fuel_efficiency):
     self.model=model
     self.fuel_efficiency=fuel_efficiency
    
   def drive(self):
      print(f"{self.model} is being driven")
      

class FuelEfficiencyCalculator:
    def calculate(self, miles, fuel):
        return miles / fuel      
       