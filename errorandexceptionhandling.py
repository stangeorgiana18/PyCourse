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
        
ask_for_int()

print('\n')

# practice ex

try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("Operands should be numbers.")

print('\n')


try:
    x = 5
    y = 0

    z = x/y
    print(z)
except:
    print("You cannot divide by zero.")
finally:
    print("All done.")

print('\n')


def ask():

    # waiting for a correct response
    waiting = True
    while waiting:
        try:
            n = int(input("Choose a number: "))
            squared_n = n ** 2
        except:
            print("An error occurred! Please try again. \n")
            continue
        else:
            waiting = False
    
    print("Your number squared is: ")
    print(n ** 2)

ask()