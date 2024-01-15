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
    def bark(self, number):
        # name gets connected to the object through self kw
        print("Woof! My name is {} and the number is {}".format(self.name, number))
        

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

my_dog.bark(11)
print('\n')


class Circle():

    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radius = 1):

        self.radius = radius

        # an attribute does not necessarily need to be defined from a particular parameter call
        # self.pi written as Circle.pi because it's a class object attribute
        self.area = radius * radius * Circle.pi

    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2

# the default value may always be overwritten
my_circle = Circle(40)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area, '\n')



# INHERITANCE AND POLYMORPHISM

# inheritance => new classes from already defined classes
# use: to reuse code and to reduce the complecity of the program

# base class
class Animal():

    def __init__(self):
        print('Animal created')
    
    def who_am_I(self):
        print("I am an animal")
    
    def eat(self):
        print("I am eating")

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    # overwrite an older method
    def who_am_I(self):
        print("I am a dog")

    def bark(self):
        print('Woof!')
    

myanimal = Animal()

# methods belong to the objects they act on

myanimal.eat()
myanimal.who_am_I()
print('\n')

mydog = Dog()
mydog.who_am_I()
mydog.bark()
print('\n')


# POLYMORPHISMS

# the way in which diff object classes can share the same method name 
# allowing you to call those same methods names without worrying about a 
# specific class that's being passed in


class Dog():

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says woof!"
    
class Cat():
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says meow!"

carl = Dog("Carl")
robin = Cat("Robin")

print(carl.speak())
print(robin.speak(), '\n')


for pet in [carl, robin]:

    print(type(pet))
    print(pet.speak())


print('\n')


def pet_speak(pet):
    print(pet.speak())

pet_speak(carl)
print('\n')


# ABSTRACT CLASSES 
# never expect to be instantiated / create an instance from this class
# designed to only serve as a base class

class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    

class Dog(Animal):
    
    def speak(self):
        return self.name + " says woof!"
    

class Cat(Animal):
    
    def speak(self):
        return self.name + " says meow!"
    

bob = Dog("Bob")
puf = Cat("Puf")

print(bob.speak())
print(puf.speak())

# eg of polymorphism
# a general open file function that take in all 
# the classes that you have and call .open on them
# it's up to the class itself the actual type of files being opened
