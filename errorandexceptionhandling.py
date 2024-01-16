# try - block to be attempted - may/not lead to an error
# except - executed if error in the try block
# finally - executed regardless of an error


def add(n1, n2):
    print(n1 + n2)

add(10, 20)

number1 = 10
number2 = input("Provide a number: ")

add(number1, number2)
print("Something happened!")

try:
    # WANT TO ATTEMP THIS CODE
    # MAY HAVE AN ERROR
    result = 10 + 10
except:
    # IF THERE'S AN ERROR
    print("It looks like you aren't adding correctly.")


print(result)