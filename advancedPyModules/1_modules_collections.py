# collections --> implements specialized container data types (dictionary, tuple)
# os module and datetime
# math and random
# python debugger
# timeit
# regular expressions
# unzipping and zipping modules


##############################
from collections import Counter


mylist = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4]
print(Counter(mylist)) # --> Counter({2: 5, 1: 3, 3: 2, 4: 1})

mylist = ['a', 'a', 'a', 'a', 10, 10, 10]
print(Counter(mylist)) # --> Counter({'a': 4, 10: 3})

# counter is a dictionary subclass -- helps count hashable objects
# inside of it: the key is the object, the value is the count

print(Counter('aaaaaabbbbbsfdfdd')) # --> Counter({'a': 6, 'b': 5, 'd': 3, 'f': 2, 's': 1})

sentence = "How many times does each word show up in this sentence with a word ?"
print(Counter(sentence.split())) # --> Counter({'word': 2, 'How': 1, 'many': 1, 'times': 1, 'does': 1, 'each': 1, 'show': 1, 'up': 1, 'in': 1, 'this': 1, 'sentence': 1, 'with': 1, 'a': 1, '?': 1})
# or print(Counter(sentence.lower(),split()))


letters = 'aaabbcccccccccdddddddddddd'

c = Counter(letters)

print(c) # --> Counter({'d': 12, 'c': 9, 'a': 3, 'b': 2})

print(c.most_common()) # --> [('d', 12), ('c', 9), ('a', 3), ('b', 2)]


# the 2 most common 
print(c.most_common(2)) # --> [('d', 12), ('c', 9)] 

# list unique elements
print(list(c)) # --> ['a', 'b', 'c', 'd']


###################################
from collections import defaultdict

d = {'a': 10}

print(d)

print(d['a'])

# DEFAULTFICT ASSIGNS A DEFAULT VALUE WHERE A KEY ERROR OCCURS
# it tries to improve on a standard dict by gettind rid of this key error 

# print(d['WRONG'])

d = defaultdict(lambda: 0) # all default values will be 0

d['correct'] = 100

print(d['correct']) # --> 100

print(d['WRONG KEY']) # --> 0

print(d)


##############################
from collections import namedtuple

# the named tuple tries to expand on a normal tuple object 
# by actually having named indices 

mytuple = (10, 20, 30)

print(mytuple[0])

Dog = namedtuple('Dog', ['age', 'breed', 'name']) # create object using oop

# nametuple(typename, field_names)
# typename -- what type this will be reported as
# field_names are passed in as a list

bobbie = Dog(age= 6, breed= 'Husky', name= 'Bob')

print(type(bobbie)) # --> <class '__main__.Dog'> 
# --> it doesn't report back it's a named tuple

print(bobbie) # --> Dog(age=6, breed='Husky', name='Bob')

print(bobbie.age)
print(bobbie.breed)
print(bobbie.name)

print(bobbie[0]) # --> 6

# for very large tuples, or where we can't remember what values at which index
# we can access them both by calling an index position such as '0' or by calling 
# it as if it was an attribute asking for 'age'


