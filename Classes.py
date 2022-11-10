#Classes
class Animal:
    def walk(self):
        print('Walking......')
class Dog(Animal): #inheritance: where the Dog class inherited the walk function from the Animal class.

    
    def __init__(self,name,age): # Constructor
        self.name = name
        self.age =  age
    def bark(self): # method 
        print('woof')

roger = Dog("Roger", 8)
print(type(roger))
print(roger.name)
print(roger.age)
roger.bark()
roger.walk()
def dog():
    print('woof!')