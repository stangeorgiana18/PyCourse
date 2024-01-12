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

my_list = [1, 2, 3, 4, 5]

from random import shuffle

shuffle(my_list)
print(my_list)

def shuffle_list(myList):
    shuffle(myList)
    return myList

result = shuffle_list(my_list)
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

print('\n')

# function practice exercises

def animal_crackers(text):
    list_words = text.lower().split()
    return list_words[0][0] == list_words[1][0]


print(animal_crackers('Levelheaded Lama'))
print(animal_crackers('Crazy cat'))
print('\n')

def makes_twenty(n1, n2):
    return (n1+n2) == 20 or n1 == 20 or n2 == 20

print(makes_twenty(10, 10))
print(makes_twenty(2, 3))
print('\n')


def old_macdonald(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper() + inbetween + fourth_letter.upper() + rest

print(old_macdonald('macdonald'))


def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize() # capitalize both strings

print(old_macdonald('macdonald'))
print('\n')


def master_yoda(text):
    inverse_text = ''
    list_words = text.split()
    reverse_word_list = list_words[::-1]
    return ' '.join(reverse_word_list) # print the string with the words from the list joined

print(master_yoda('I am home'))
print('\n')


def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

print(almost_there(104))
print(almost_there(150))
print('\n')


def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

print('results for has_33:')
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print('\n')


# or slice the list with nums[i:i+2]:
def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i:i+2] == [3, 3]:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print('\n')


def paper_doll(text):
    new_text = ''
    for char in text:
        new_text += char*3
    return new_text

print(paper_doll('Hello'))
print('\n')


def blackjack(a, b, c):
    if sum([a, b, c]) <= 21: 
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        return sum([a, b, c]) - 10
    else:
        return 'BUST'
        
print(blackjack(5,6,7))
print(blackjack(9, 9, 9))
print('\n')

# a tricky one

def summer_69(arr):

    total = 0
    add = True
    
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break

    return total

print('summer_69:')
print(summer_69([2, 1, 6, 9, 11]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print('\n')


# true if the list of integers contains 007 in order,
# not necessarily on consecutive positions

def spy_game(nums):

    code = [0, 0, 7, 'x']
    # [0, 7, 'x']
    # [7, 'x']
    # ['x'] length = 1
    for num in nums:
        if num == code[0]:
            code.pop(0)  # pop off the first item

    return len(code) == 1

print('spy_game:')
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
print('\n')



##############################################
# USE OF FOR ELSE STATEMENT - unique in python
##############################################

def count_primes(num):

    # check for 0 or 1 input
    if num < 2: 
        return 0
    ##############
    # 2 or greater
    ##############

    # clever trick
    # store our prime numbers 
    primes = [2]
    # counter going up to the input num
    # if I start off with 3 I can make the step size 2
    x = 3

    # x is going through every number up to the input number
    while x <= num:
        # check if x is prime
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        # else aligned with for because I have a break inside the for
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print('count_primes:')
print(count_primes(100))


# another way:
def count_primes(num):
    
    if num < 2: 
        return 0
    
    primes = [2]
    x = 3

    while x <= num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(100))
print('\n')



# print out function that takes in a single letter

def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print('print_big:')
print_big('a')
      



##################################
# Lambda functions 
# anonymous one time use functions 
# and then never referenced again
###################################

def square(num):
    return num**2

my_nums = [4, 7, 13, 14]

# for map function you pass in the function that you want to map
# to every single element or item in this list

print(map(square, my_nums))
# output: <map object at 0x104ef61d0> -> this is a memory location

# iterate through the map function:
# apply the square function to every item in my_nums / or any iterable
for item in map(square, my_nums):
    print(item)

print('get the actual list:')
print(list(map(square, my_nums)))
print('\n')




def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    else:
        return mystring[0]

names = ['Serban', 'Georgi', 'Laura']

# pass the function without .() because map is going to execute it itself
print(list(map(splicer, names)))






#################################################################
# FILTER function
# returns an iterator yielding those items of the iterable
# for which when you pass in the item into the function, it's true
#################################################################

# create a function that returns either true or false

def check_even(num):
    return num % 2 == 0

my_nums = [12, 44, 64, 2, 3, 51]

print(filter(check_even, my_nums))

result = list(filter(check_even, my_nums))
print(result)

for n in filter(check_even, my_nums):
    print(n)

print('\n')





# LAMBDA EXPRESSIONS

def square(num): return num ** 2

print(square(3))

        
