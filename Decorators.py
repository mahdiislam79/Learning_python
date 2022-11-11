# Decorators
# A decorator is a function that takes a function as an input and wraps it in another function as an inner function.

def logtime(func):
    def wrapper(a,b):
        sum = a + b
        print(sum)
        val = func()  # assigning the function as val and then adding some more properties to the wrapper function
        print('after')
        return val
    return wrapper
    
@logtime # by using this command we are wrapping the hello() function as an inner function in logtime as a function called wrapper. 
def hello():
    print("Hello")
hello(5,6)    