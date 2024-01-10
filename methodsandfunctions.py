# methods = functions that are built into objects

# methods in built-in objects:
myList = [1, 2, 3]
myList.append(4)
print(myList)
print(myList.pop())

# control + space -> methods available for the object

# get the documentation of the object 
# help(myList.insert) # obtain a docstring 


# functions use snake casing for naming
# class calls use camel casing 


# return is like break out of the function


numList = [12, 34, 22]
def check_even_list(numList):
    for number in numList:
        if number % 2 == 0:
            return True
        else:
            # pass useful for functions that need/require multiple return statements
            pass  # return here - wrong!
    return False

print(check_even_list(numList))

def even_numbers_list(numList):
    # placeholder variables
    evenNumbers = []
    for number in numList:
        if number % 2 == 0:
            evenNumbers.append(number)
        else: 
            pass

    return evenNumbers

print(even_numbers_list(numList))
print(even_numbers_list([1, 3, 5]))

# functions and tuple unpacking

stock_prices = [('Apple', 200), ('Google', 500)]
for ticker, price in stock_prices:
    print(price + (0.1 * price))


# unpack the result from a function
work_hours = [('Monday', 15), ('Tuesday', 8), ('Wednesday', 14)]
def consistency_check(work_hours):
    current_max = 0
    most_productive_day = ''
    
    for day, hours in work_hours:
        if hours > current_max:
            current_max = hours
            most_productive_day = day
        else:
            pass

    return (most_productive_day, current_max) # return a tuple

items = consistency_check(work_hours)
print(items) # to inspect the number of variables


# interactions between functions

list = [1, 2, 3, 4, 5]

from random import shuffle

shuffle(list)
print(list)

def shuffle_list(myList):
    shuffle(myList)
    return myList

result = shuffle_list(list)
print(result)


# three cup monte

myList = [' ', 'O', ' '] # guess where is the hidden O
shuffle(myList)
print(myList)

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('pick a number: 0, 1 or 2: ') 

    # input always returns a string
    # this is why int is used here
    return int(guess)

# my_index = player_guess()
# print(my_index)

def check_guess(myList, guess):
    if myList[guess] == 'O':
        print('correct')
    else:
        print('wrong guess')
        print(myList) # tell the user what it actually was

# script 
# initial list
myList = [' ', 'O', ' ']

# shuffle list
mixedup_list = shuffle_list(myList)
        
# user guess
guess = player_guess()
        
# check guess
check_guess(mixedup_list, guess)




# functional parameters: *args and **kwargs
# these stand for arguments and keyword arguments

def myfunc(a, b):
    # return 8% of the sum of a and b
    return sum((a, b)) * 0.08

# a and b are positional arguments
# eg. 20 assigned to a because it was in the 1st position
print(myfunc(20, 30))


# args allows to treat this as a tuple of parameters that are coming in
# args is used to pass a variable no. of arguments to a function
# it can be any word as long as it has *, for eg. *spam,..
# by convention, *args should be used

def myfunc(*args):
    print(args) # looks as a tuple
    return sum(args) * 0.05

print(myfunc(40, 70, 20, 204))

def myfunc(*args):
    for item in args:
        print(item)

myfunc(40, 70, 20, 204)
print('\n')



# handle an arbitrary no. of keyworded arguments 
# **kwargs builds a dictionary of key value pairs 
# instead of creating a tuple of values

def myfunc(**kwargs):
    print(kwargs)
    if 'vegetable' in kwargs:
        print('my vegetable of choice is {}'.format(kwargs['vegetable'])) # kwargs will take the value corr. to the key
    else:
        print('no vegetable found here')

myfunc(vegetable = 'cucumber', fruit = 'strawberry')

# print(kwargs) gives: {'vegetable': 'cucumber', 'fruit': 'strawberry'}


# *args returns a tuple
# **kwargs returns a dictionary

# use in combination

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)

    print('I would like {} {}'.format(args[0], kwargs['food']))

myfunc(10, 22, 32, fruit = 'orange', food = 'eggs', animal = 'dog')


# this allows to take in an arbitray number of arguments that you don't need to define beforehand
# especially useful when you begin to use outside libraries




# other exercise

def myfunc(string):
    out = ''
    for i in range(len(string)):
        if i % 2 == 0:
            out += string[i].upper()
        else:
            out += string[i].lower()
    return out

print(myfunc('Anthropomorphism'))


