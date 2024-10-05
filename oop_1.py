# Object Oriented Programing in Python

class Dog:
    def __init__(self,name,age): 
        self.name = name
        self.age = age
    @staticmethod # if we use @staticmethod we dont need to use self.
    def add_one(x):
        return x + 1
    
    def add_two(self,x):
        return x + 2
    
    def hello(self):
        print("Hello")
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
        
d = Dog("H",3)
print(d.add_two(5))
    