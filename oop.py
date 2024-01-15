# important for flexibility
# objects may be also called classes in python
# self word to connect the method to the instnace of the class

# ATTRIBUTES AND CLASS KEYWORD

mylist = [1, 2, 3]
myset = set()
print(type(mylist))

# class = blueprint that defines the nature of a future object
# from classes, we can construct an instance of the object 
# an instance = a specific object created from a particular class

class Dog():

    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    '''
    init is a constructor for a class, 
    called automatically when creating an instance of the class
    self keyword is the instance of the object itself
    '''
    def __init__(self, breed, name):
       
       # ATTRIBUTES
       # we take in the argument
       # assign it using self.attribute_name

       self.breed = breed
       self.name = name

    # OPERATIONS/Actions ---> Methods
    def bark(self):
        # name gets connected to the object through self kw
        print("Woof! My name is {}".format(self.name))
        

my_dog = Dog('Huskie', "Marcel")
print(type(my_dog))

print(my_dog.species)
print(my_dog.name)

# methods - functions acting on an object, that take the object itself into account
# through the use of self argument/keyword

# attributes don't have parantheses -> they are not executed 
# they are just sth characteristic to the object that you call back

# methods need to be executed
# it is an action the object can take

my_dog.bark()