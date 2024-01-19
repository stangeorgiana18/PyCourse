# generator functions allows us to write a function that can send back
# a value and then later resume to pick up where it left off

# --> sequence of values generated over time 
# instead of having to create an entire seq and hold it in memory
# yield statement as the main syntax difference 

# a compiled generator function becomes an object supporting an interation protocol
# they don't return a value and then exit 

def create_cubes(n):

    for x in range(n):
        yield x ** 3


# more memory efficient now
# generating the values as you need them
        
for x in create_cubes(10):
    print(x) # one value at a time

print(create_cubes(10)) # --> you need to iterate through it if you actually want the list of no.


# calculate a fibonacci sequence 

def gen_fibon(n):

    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b # tuple matching

for number in gen_fibon(10):
    print(number)

# difference between yielding and creating a normal function

def gen_fibon(n):
    
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a, b = b, a + b # tuple matching

    return output


for number in gen_fibon(10):
    print(number)


# key to understanding generators: next and iter function

###############
# NEXT FUNCTION
###############

def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # --> error: all the values have been yielded


###############
# ITER FUNCTION
###############

# automatically iterate through a normal object that you may not expect

s = 'hello'

for letter in s:
    print(letter)

# print(next(s)) # --> error: it supports iteration but we cannot directly iterate over it

# transform the string into a generator
# iter() -- CONVERT ITERABLE OBJECTS INTO ITERATORS THEMSELVES:

print('\n')

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))



# Iterables are any objects you can get an iterator from.
# Iterators are objects that let you iterate on iterables.


# practice ex

print('\n')

def gensquares(N):

    for x in range(N):
        yield x ** 2

for x in gensquares(10):
    print(x)

print('\n')


# create a generator that yields "n" random numbers between a low and high number (that are inputs)

import random

print(random.randint(1,10))

def rand_num(low, high, n):
    
    for numbers in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print(num)

print('\n')


# use the iter() function to convert the string below into an iterator

string = "python"

string = iter(string)

print(next(string))

print('\n')


# explain what gencomp is in the code below

my_list = [1,2,3,4,5]

# generator comprehension - list comprehension, but generate it instead of saving it in memory
# SQUARE BRACKETS SWITCHED OUT TO PARANTHESES => turn the lc into a generator:

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
    