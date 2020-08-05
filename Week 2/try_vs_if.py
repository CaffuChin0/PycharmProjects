
try:
    number = int(input("Enter a number: "))
    print("The number you keyed in is: ", number)
except ValueError:
    print("I am expecting a number")

number_string = input("Enter a number: ")
if(number_string.isdigit()):
    number = int(number_string)
    print("The number you keyed in is: ", number)
else:
    print("I am expecting a number")