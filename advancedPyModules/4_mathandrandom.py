#############
# MATH MODULE
#############

import math

# what's available in math?
#help(math)

value = 4.5

integer = math.floor(value)
print(integer)

next_integer_up = math.ceil(value)
print(next_integer_up)

print(round(4.35))
print(round(4.5)) # 4
print(round(5.5)) # 5
print(round(6.5)) # 6

# choose to round all to either all evens or all odds

print(math.pi)

from math import pi

print(pi)
print(math.e)

print('\n')

print(math.inf)
print(math.nan)

############
# HEAVY MATH -- USING MATH.INF OR MATH.NAN -- CHACK OUT THE NUMPY LIBRARY 
# NumPy -- library specifically designed for numnerical processing
# highly efficient and goes much deeper than Py's built-in math module
############

print(math.log(math.e)) # 1.0

power = math.log(100, 10)
print(power) # 2.0

radians = math.sin(10)
print(radians)

degrees = math.degrees(pi/2)
print(degrees)

radians = math.radians(180)
print(radians, '\n') # pi


###############
# RANDOM MODULE
###############

import random

random_int = random.randint(0, 100)
print(random_int, '\n')

# SETTING A SEED -- allows us to start from a seeded pseudo-random number generator 
# which means the same random numbers will show up in a series 

# usually 101 or 42 as seed 
random.seed(101)


# set a seed for any sequence of basically infinite random numbers
print(random.randint(0, 100)) # 74
print(random.randint(0, 100)) # 24
print(random.randint(0, 100)) # 69
print(random.randint(0, 100), '\n') # 45

mylist = list(range(0, 20))

# choose a random int from the list 
print(random.choice(mylist))

# SAMPLE WITH REPLACEMENT 

# pick a number ten times and return a list of those no.
random_list = random.choices(population= mylist, k= 10)
print(random_list)

# SAMPLE WITHOUT REPLACEMENT -- an item once picked cannot be picked again
random_list = random.sample(mylist, 10)
print(random_list)


# shuffle a list -- this will permanently affect the list
# so you don't have to assign the result to anything
# the list is shuffled in place
random.shuffle(mylist)
print(mylist, '\n')


# PROBABILITY DISTRIBUTIONS:

# pick a value between a and b
# CONTINUOUS DISTRIBUTION -- FLOATING POINT NUMBERS ARE ALLOWED 
# called UNIFORM because every number > a, < b has the same likelihood of being chosen

random_number = random.uniform(a= 0, b= 100)
print(random_number)



# NORMAL/GAUSSIAN DISTRIBUTION:

# takes in a mean and standard deviation
random_number = random.gauss(mu= 1, sigma= 1)
print(random_number)


# if you're calling random.uniform/random.gauss you should start swithcing to NumPy at that point
