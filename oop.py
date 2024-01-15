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
print(puf.speak(), '\n')

# eg of polymorphism
# a general open file function that take in all 
# the classes that you have and call .open on them
# it's up to the class itself the actual type of files being opened



# SPECIAL METHODS / MAGIC METHODS / DUNDER METHODS

# use built in functions with user-defines objects

mylist = [1, 2, 3]

len(mylist)

class Sample():
    pass

mysample = Sample()
print(mysample, '\n')


class Book():

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    # if there's ever a function that asks for a string representation of your book class
    # then it's going to return what this method returns 
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # return the length of user-defined objects
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted.")


b = Book("Evrika", 'Geo', 345) 

# print fucnction asks what's the string representation of b
print(b) 

print(str(b))

print(len(b), '\n')

del b

# delete a book: del b
# delete variable from the computer's memory

print('\n')


# revision exercises

class Cylinder():

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.14 * (self.radius ** 2) * self.height
    
    def surface_area(self):
        return 2 * 3.14 * self.radius * self.height + 2 * 3.14 * (self.radius ** 2)
    

c = Cylinder(2, 3)

print(c.volume())
print(c.surface_area(), '\n')



class Line():

    def __init__(self, coor1, coor2):
        self.coor1_x = coor1[0]
        self.coor1_y = coor1[1]
        self.coor2_x = coor2[0]
        self.coor2_y = coor2[1]
     
    def distance(self):
    
        return ((self.coor2_x - self.coor1_x) ** 2 + (self.coor2_y - self.coor1_y) ** 2) ** 0.5
    
    def slope(self):
        
        return (self.coor2_y - self.coor1_y) / (self.coor2_x - self.coor1_x)
    

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope(), '\n')


# methods that affect attributes 

class Simple():

    def __init__(self, value):
        
        self.value = value
    
    def add_to_value(self, amount):
        
        self.value = self.value + amount
        print('We just added {} to your value'.format(amount))

    
myobj = Simple(300)

print(myobj.value)

print(myobj.add_to_value(500))
print(myobj.value, '\n')


# bank account class

class Account():

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        print(f"Deposit Accepted: added ${deposit} to the balance.")

    def withdraw(self, withdrawal):
        if self.balance < withdrawal:
            print("Funds Unavailable!")
        else:
            self.balance -= withdrawal
            print("Withdrawal accepted!")

    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: ${self.balance}"
    

# 1. Instantiate the class
acct1 = Account('Geo', 400)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
print(acct1.owner)

# 4. Show the account balance attribute
print(acct1.balance)

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)