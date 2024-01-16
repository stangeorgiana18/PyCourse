# try - block to be attempted - may/not lead to an error
# except - executed if error in the try block
# finally - executed regardless of an error


try:
    # WANT TO ATTEMP THIS CODE
    # MAY HAVE AN ERROR
    result = 10 + 10
except:
    # IF THERE'S AN ERROR
    print("It looks like you aren't adding correctly.")
else:
    # if there's no exception/error there
    print("Add went well.")
    print(result)


# see built-in exceptions in the documentation
try:
    f = open("testfile", w)
    f.write("Ce interesant")
except TypeError:
    print("There was a type error!")
except OSError:
    # if opening a file you don't have permission to
    print("You have an OS Error")
finally:
    # execute no matter what
    print("I always run.")
    
