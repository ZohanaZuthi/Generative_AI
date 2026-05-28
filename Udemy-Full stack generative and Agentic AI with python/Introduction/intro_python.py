class Chai:
    # to initialize or preparation method we have to write __init__ method in python class
    def __init__(self,name, age):
        self.name=name
        self.age=age
    
    def Location(self, loc):
        print(f"{self.name} is currently in {loc}")
    
    def introdc(self):
        print(f"{self.name} is {self.age} years old")
        
chai1=Chai(name="Zuthi", age=24)

chai1.Location("Dhaka")
chai1.introdc()