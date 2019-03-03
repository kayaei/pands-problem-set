# Etem Kaya 22-Feb-2019

# First solution to Problem-1 (Solution-1b)
# Fine name: "sumupto-1b.py".

# Problem-1: Write a program that asks the user to input 
# any positive integer less than 100 and outputs the 
# sum of all numbers between one and that number.

# execute the code until a positive integer with less than 3 digit entered.
while True:
# execute code between try - except block and catch errors at except function.
    try:
        # declare an integer type user input variable.
        i = int(input("Please enter a positive integer less than 100: "))

        # max 2 digits allowed to prevent crashes when large numbers entered. 
        if 0 <= i < 100: # check a positive integer with less than 100 entered.
            # add all numbers from 0 upto that number entered and display it.
            print("The sum is", sum(range(i+1))) 
            break # terminate the loop to end the program.
        # when number entered is outside the allowed range.
        else:
            print("A positive integer > 99 or a negative integer entered")
            print("Please try again.")
            continue # go to while True and continue executing the code

    # catch any error which is not a positive integer.
    except:
    # an unacceptable value detected.
        print("this is not a positive integer number. Please try again.")