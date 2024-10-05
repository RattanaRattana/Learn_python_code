class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
        
    def speak(self):
        print("I dont know what I say")
        
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # call variable name and age from Pet class (parents class)
        self.color = color
    def speak(self):
        print("Meow")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and color {self.color}")
        
class Dog(Pet):
    def speak(self):
        print("Bark")
        
class Fish(Pet):
    pass
        
c = Fish("Tim",19)
c.speak()
        