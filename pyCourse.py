# opening and reading files

file = open('file.txt')
print(file.read()) # read the file as an individual string
print(file.read()) # nothing as output, cursor needs reset

file.seek(0) # reset de cursor 
print(file.read()) # return strings line by line 

file.seek(0)
print(file.readlines()) # return list of strings

# otherFile = open("/Users/georgianastan/Desktop/my python stuff/file.txt")
file.close() # so that Python doesn't use this file anymore

# reading and writing to a file

# mode 
# a for appending only
# r+ for reading + writing
#w+ for writing + reading (overwriting)
    
with open('file.txt', mode = 'a') as myFile:
    myFile.write("\nPython e misto")

with open('file.txt', mode = 'r') as myFile:
    print(myFile.read())

with open('createdFile.txt', 'w') as f:
    f.write("yey")

with open('createdFile.txt', 'r') as f:
    print(f.read())

# ex with data structures
    
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

list4 = [5,3,4,6,1]
list4.sort()
print(list4)

d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])


# for loops

myList = [1, 2, 3, 4, 5]
for n in myList:
    print('yupy')

# iterate without a variable
for _ in "hello":
    print("great")

# tuple unpacking - duplicate the items of the sequence and unpack them
myList = [(1,2), (3, 4), (5, 6)]
for (a, b) in myList:
    print(a)
    print(b)

for a, b in myList:
    print(b)

d = {'k1': 1, 'k2': 2, 'k3': 3}

# iterate through the keys, by default iterating through a dict
for item in d:
    print(item)

# iterate through the items
for _ in d.items():
    print(_)

for key, value in d.items():
    print(key)

for value in d.values():
    print(value)

# pass a syntax placeholder to avoid syntax error
x = [23, 4, 21]
for item in x:
    # avoid syntax error
    pass
print('end')

myString = "Georgi"
for letter in myString:
    if letter == "e":
        # go ahead and go back to the loop
        continue
    print(letter)


print(list(range(0, 15, 3)))

indexCount = 0
for letter in 'longnumber':
    print('at index {} the letter is {}'.format(indexCount, letter))
    indexCount += 1

# replicate the above loop using enumerate

indexCount = 0
word = 'heyheyhey'
for letter in word:
    print(word[indexCount])
    indexCount += 1

# enumerate returns the index counter and 
# the object itself or element at that particular iteration
    
word = 'yupy'
for item in enumerate(word):
    print(item) # output: index count automatically in the form of tuples

# further, tuple unpacking
word = 'beauty'
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# the opposite of enumerate - the zip functions
# zip together 2 lists
    
myList1 = [13, 23, 43, 64, 78, 98]
myList2 = ['u', 'd', 'p', 's']
myList3 = [234, 343, 832, 901]

for item in zip(myList1, myList2, myList3):
    # zip together the lists and pair up the items
    print(item) # obtain list of tuples

# if the lists are uneven, zip will only be able to go
# and zip together as far as the list which is the shortest

# obtain the zip list itself 
print(list(zip(myList1, myList2, myList3)))

# [(13, 'u', 234), (23, 'd', 343), (43, 'p', 832), (64, 's', 901)]

# unpack the tuples again
for a, b, c in zip(myList1, myList2, myList3):
    print(b) # elements of the second list



# the in operator 
print('x' in ['x', 'y', 'z'])

print('a' in 'final')

# the in operator works in dictionaries as well
print('mykey' in {'mykey': 7887})

d = {'mykey': 7887}
print(7887 in d.values())
print(7887 in d.keys())

# min, max and random numbers
myList = [13, 24, 4656, 345]
print(min(myList))
print(max(myList))



from random import shuffle

myList = [39, 90, 290, 230, 123]

shuffle(myList) # it does not return anything
print(myList)

print(type(shuffle(myList))) # none tyoe
# shuffle is an in-place function - operated in-place on the list



# grab a random integer 

from random import randint

print(randint(0, 100))
print(randint(0, 100))

randomNumber = randint(220, 323)
print(randomNumber)

# accept user input with the input function - accepts only strings
answer = input('do you remember this?: ')
print(answer)

number = input('numbers are returned as strings too: ')
print(number)
print(type(number)) # str

# transform the result (number) in other data type 
print(float(number))
print(int(number))

number = int(input('other number: '))
print(number)
print(type(number))


# list comprehension 
# good alternative to for loop along with .append() to create a list

myString = 'walnut'
myList = []
# make a list of every character

for letter in myString:
    myList.append(letter)
print(myList)

print('\n')


# using list comprehension, but computationally the same 
# essentially it's a flattened out for loop
# letter + the for first line
# [take element for element in other iterable object]

myList = []
myList = [letter for letter in myString]
print(myList)

myList = [eat for eat in 'chocolate']
print(myList)

# perfom operations on the first variable name
myList = [num**2 for num in range(23, 34, 2)]
print(myList)


myList = [x**2 for x in range(22, 90) if x % 2 == 0]
print(myList)

print('\n')

celcius = [0, 12, 23, 22]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

# readibility and reproducibility - the most important

# use if and else statement inside of a list comprehension 
results = [x if x % 2 == 0 else 'ODD' for x in range(45, 87)]
print(results)


# nested loops in a list comprehension
myList = []
for x in [8, 12, 14]:
    for y in [1, 10, 1000]:
        myList.append(x*y)

print(myList)

print('\n')

# othewise the above
myList = [x*y for x in [8, 12, 14] for y in [1, 10, 100]]
print(myList)


