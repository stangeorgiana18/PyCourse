
# use the python debugger to set a trace

import pdb

x = [1, 2, 3]
y = 2
z = 3

# a trace is going to pause operations mid script and allow you to play
# with variables to understand what's going on
# SET THE TRACE BEFORE THE ERROR LINE 
result_one = y + z

pdb.set_trace() # => a little interactive environment
# I can call variables to check what they are 
# or perform other operations, x + y

result_two = y + x


