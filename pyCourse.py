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

