def func():
    return 1

print(func())

# we can assign functions to other variables and then execute them off that variable

def hello():
    return "hello!"

#greet = hello

#print(greet(), '\n')

# did greet make its own copy of the hello function or just pointed to hello?
# test by deleting hello and see if we can still call greet

del hello

#print(greet())

# passing in a function within another function

def hello(name = "Geo"):
    print("The hello() function has been executed!")

    def greet():
        return '\t This is a greet() function inside hello!'
    
    def welcome():
        return '\t This is welcome() inside hello.'
    
    
    print("I am going to return a function!")

    # this would allow assiging a function to a variable
    if name == "Geo":
        return greet
    else:
        return welcome

 
my_new_func = hello("Geo") # pointed to the greet function inside hello
print(my_new_func())

def cool():

    def super_cool():
        return "I am very cool!"
    
    return super_cool

some_func = cool()

print(some_func(), '\n')


# calling functions within another function

def hello():
    return 'Hi, Geo!'


def other(some_def_func):
    print('Other code runs here!')

    # passing a function as an argument 
    print(some_def_func())

other(hello)
print('\n')

# hello when it's passed in as raw function
# hello() when it's executed --> 'Hi, Geo!'


########################
# CREATE A NEW DECORATOR
########################

def new_decorator(original_func):

    # the extra functionality you want to decorate the original function with
    def wrap_func():
        print("Some extra code, before the original func.")

        original_func()

        print("Some extra code after the original func.")

    return wrap_func

# idea behind: a present with wrapping paper
# the original function is the present 
# put into a box and wrap around it --> decoration (the code before/after the original())

def func_needs_decorator():
    print("I want to be decorated!")


func_needs_decorator()
print('\n')

decorated_func = new_decorator(func_needs_decorator)

print(decorated_func(), '\n')


# create a new decorator using special syntax @
# pass the function below into the @function as an argument

@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()

# decorators -- commonly used in web frameworks: Django, Flask
# usually used to render a new website or point to another page

# Flask -- used to create web pages in Python
# decorators are highly integrated in the way the framework works

# Django -- more heavy-duty and popular web framework for Python


