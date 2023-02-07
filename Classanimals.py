

class Smallanimals:
    def __init__(self , name, age ) :
       self.name =name 
       self.age = age
    def walk (self):
        print( f" {self.name} walk")
class Dog (Smallanimals):
   def special_speak (self) :
       return( "the dog speak")

class Cat(Smallanimals) :
    pass 
dog = Dog( "zizo" , 2)
print( dog.special_speak())
dog.walk()
cat = Cat("kiko" , 1)
cat.walk()
