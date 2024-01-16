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
# usual blocks:
    
try:
    f = open("testfile", 'r')
    f.write("Ce interesant")
except:
    print("All other exceptions!")
finally:
    # execute no matter what
    print("I always run.")


def ask_for_int():

    while True:
        try:
            result = int(input("Provide a number: "))
        except:
            print("That is not a number.")
            continue
        else:
            print("Yes, thank you for the integer.")
            break
        finally:
            print("End of try/except/finally.")
            print("I will always run at the end.")

ask_for_int()