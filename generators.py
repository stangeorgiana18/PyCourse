# generator functions allows us to write a function that can send back
# a value and then later resume to pick up where it left off

# --> sequence of values generated over time 
# instead of having to create an entire seq and hold it in memory
# yield statement as the main syntax difference 

# a compiled generator function becomes an object supporting an interation protocol
# they don't return a value and then exit 

def create_cubes(n):

    result = []
    for x in range(n):
        result.append(x ** 3)
    
    return result

for x in create_cubes(10):
    print(x) # one value at a time


