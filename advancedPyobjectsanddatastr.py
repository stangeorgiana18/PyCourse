# ADVANCED NUMBERS

print(hex(12))
print(hex(196), '\n')

print(bin(128))
print(bin(196), '\n')

print(pow(2, 4))
print(pow(2, 4, 3), '\n') # third arg treated as a mod: 2**4 % 3

print(abs(-3.4))
print(round(4.3)) # round returns the int 
print(round(5), '\n')
print(type(round(4.3)))

# specify how many digits you want after decimal points
print(round(3.141592, 2))
print(type(round(3.141592, 2))) # float
print('\n')


# ADVANCED STRINGS

s = "hello geo"
print(s.capitalize())
print(s.upper())
print(s.lower(), '\n')

print(s.count('o'))
print(s.find('o'))

print('\n', s)
# place s in between a bunch of z and the total length is 20
print(s.center(20, 'z'))
print('\n') 

print('hello\thi'.expandtabs(8)) # replace tab char with spaces, by default 8 if no number provided
print('\n')

s = 'hello'
print(s.isalnum()) # check if all characters alphanumberic
print(s.isalpha()) # check if all characters alphabetic; useful in natural language processing techniques
print(s.islower()) # at least one character in s and if all case char are lowercase

print('\n')
print(s.isspace()) # check if all char are white space
print(s.istitle(), '\n') # check is s is a title case string -- each word is captitalized 
# uppercase char only follow uncased and lowercase only follow cased ones

print('HELLO'.isupper(), '\n')

print(s.endswith('o'), '\n') # if s[-1] == 'o'


# split returns a list
# splits at every instance
print(s.split('e')) # ['h', 'llo']

s = 'hihihhhhiiiihihii'
print(s.split('i')) # ['h', 'h', 'hhhh', '', '', '', 'h', 'h', '', '']

# partition returns a tuple
# split only at the first instance 
print(s.partition('i'), '\n') # ('h', 'i', 'hihhhhiiiihihii')


# ADVANCED SETS

s = set()

s.add(1)
s.add(2)

s.clear() # delete all char from the set

print(s)

s = {1, 2, 4}
sc = s.copy()

s.add(5)

print(s)
print(sc)

# difference of 2 or more sets
# return the dif element
print(s.difference(sc), '\n')

set1 = {1, 2, 3}
set2 = {1, 4, 5}

# return the first set after removing all the elements found in the second one 
set1.difference_update(set2)
print(set1) # {2, 3}

s.discard(2)
s.discard(12) # no error if the number not in the set
print(s, '\n')

s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1.intersection(s2))

# make the first set equal to the intersection
s1.intersection_update(s2) 
print(s1)

s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}

# .isdishoint() -- true if the 2 sets have a null intersection
print(s1.isdisjoint(s2)) # False
print(s1.isdisjoint(s3), '\n') # True

# check if s1 is a subset of s2
print(s1.issubset(s2))

# check if s2 contains s1
print(s2.issuperset(s1), '\n')

# symmetric difference -- all the elements that are exactly in one of the sets
# the opposite of intersection

print(s1.symmetric_difference(s2)) # {4}

# change s1 into the symmetric diff
s1.symmetric_difference_update(s2)
print(s1)

print(s1.union(s2))

# update the set with the union of itself and others 
s1.update(s2) 
print(s1, '\n') # {1, 2, 4}


# keep SETS in mind when doing comparisons or looking for unique values


# ADVANCED DICTIONARIES 

d = {'k1': 1, 'k2': 2}

# create a disctionary through dictionary comprehension
print({x: x ** 2 for x in range(10)}) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# assign keys that are not based on the values 
print({k: v ** 2 for k, v in zip(['a', 'b'], range(2))})

for k, value in d.items():
    print(k, value)

print('\n')

# ADVANCED LISTS
    
l = [1, 2, 3]
l.append(4)

print(l.count(10))
print(l.count(1))

x = [1, 2, 3]
x.append([4, 5])
print(x) # [1, 2, 3, [4, 5]]

# extend a list into an original list
x = [1, 2, 3]
x.extend([4, 5]) # appends items individually from the iterable
print(x) # [1, 2, 3, 4, 5]

print(l.index(2), '\n') 
# error if indexing an element that's not in the list

# at index 2 insert a string called inserted
l.insert(2, 'inserted')
print(l) # [1, 2, 'inserted', 3, 4]

ele = l.pop()
print(ele) # 4
print(l) # [1, 2, 'inserted', 3]

l.pop(0)
print(l) # [2, 'inserted', 3]

# remove the first occurrence of a value
l.remove('inserted')
print(l) # [2, 3]

l = [1, 2, 3, 4, 3]
l.remove(3)
print(l) # [1, 2, 4, 3]

l.reverse()
print(l) # [3, 4, 2, 1]

l.sort()
print(l) # [1, 2, 3, 4]
