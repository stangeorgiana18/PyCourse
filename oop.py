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
    def __init__(self, breed, name, spots):
       
       # ATTRIBUTES
       # we take in the argument
       # assign it using self.attribute_name

       self.breed = breed
       self.name = name

       # expect boolean True/False
       self.spots = spots

    # OPERATIONS/Actions ---> Methods
    def bark(self):
        print("Woof!")
        

my_dog = Dog(breed = 'Lab', name = "Marley", spots = False)
print(type(my_dog))

print(my_dog.species)

# methods - functions acting on an object, that take the object itself into account
# through the use of self argument/keyword

