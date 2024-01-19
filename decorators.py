def func():
    return 1

print(func())

# we can assign functions to other variables and then execute them off that variable

def hello():
    return "hello!"

greet = hello

print(greet(), '\n')

# did greet make its own copy of the hello function or just pointed to hello?
# test by deleting hello and see if we can still call greet

del hello

print(greet())

# passing in a function within another funcion

def hello(name = "Geo"):
    print("The hello() function has been executed!")

hello()

# calling functions within another function