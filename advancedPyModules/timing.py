def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))

def func_two(n):
    return list(map(str, range(n)))

print(func_two(10))

import time 

# CURRENT TIME BEFORE RUNNING THE CODE
start_time = time.time()

# RUN CODE
result = func_one(1000000)

# CURRENT TIME AFTER RUNNING CODE
end_time = time.time()

# ELAPSED TIME 
elaspsed_time = end_time - start_time

print(elaspsed_time)



start_time = time.time()
result = func_two(1000000)
end_time = time.time()
elaspsed_time = end_time - start_time
print(elaspsed_time, '\n')

# for code that runs fast the precision may not be enough to show anything: 0.0


# TIMEIT MODULE

import timeit

stmt = '''
func_one(100)
'''

# what code needs to be run before you call statement over and over again
# setup runs everything once to set it up for the statement code 
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number = 1000000))

stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
    return list(map(str, range(n)))
'''

print(timeit.timeit(stmt2, setup2, number = 1000000))
