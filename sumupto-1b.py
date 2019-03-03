# Etem Kaya 22-Feb-2019

# First solution to Problem-1 (Solution-1b)
# Fine name: "sumupto-1b.py".

# Problem-1: Write a program that asks the user to input 
# any positive integer less than 100 and outputs the 
# sum of all numbers between one and that number.

# execute the code until a positive integer with less than 3 digit entered.
while True:
# eexecute the code between try and except block and catch any errors at the except function.
    try:
        # declare a user input variable to integer type.
        i = int(input("Please enter a positive integer less than 100: "))

        # max of 2 digit numbers allowed to prevent program crashing when large numbers entered. 
        if 0 <= i < 100: # check a positive integer with less than 3 digits entered.
            print("The sum is", sum(range(i+1))) # add up all numbers from 0 upto the number entered.
            break # terminate the loop to end the program.
        else:
            # number entered is outside the allowed range.
            print("A positive integer but greater than 99 or a negative integer entered, please try again.")
            continue # go to while True and continue executing the code

    # catch any error which is not a positive integer.
    except:
    # an unacceptable value detected.
        print("this is not a positive integer number, please try again.")