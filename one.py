# python one.py
print('hello')

# built-in variable 
# py does this in the background:
# it assigns the string to the name variable when run directly
# __name__ = "__main__"

def myfunc():
    pass

# the way to organize the code at the bottom based on what you want to execute
if __name__ == "__main__":
    myfunc()
