#Classes
class Animal:
    """ A class representing an Animal """
    def walk(self):
        print('Walking......')
class Dog(Animal): #inheritance: where the Dog class inherited the walk function from the Animal class.
    """ A class representing a dog where it inherits the characteristics of Animal function"""
    def __init__(self,name,age): # Constructor
        """ Initialize a new dog"""    
        self.name = name
        self.age =  age
    def bark(self): # method 
        """Let the dog bark"""
        print('woof')

roger = Dog("Roger", 8)
print(type(roger))
print(roger.name)
print(roger.age)
roger.bark()
roger.walk()
def dog():
    print('woof!')
    
print(help(Dog))