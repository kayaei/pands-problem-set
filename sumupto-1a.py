# Etem Kaya 22-Feb-2019
# Solution-1a: Problem-1 first solution - "sumupto-1a.py".
"""
Problem-1: Write a program that asks the user to input 
any positive integer less than 100 and outputs the 
sum of all numbers between one and that number.
"""

while True: 
# execute the code until a positive integer with less than 3 digit entered.
    try:
        i = eval(input("Please enter a positive integer less than 100: ")) # evaluate the values entered.

        if type(i) == str: # check if a string value entered.
            print("You entered a string. Please try again.")
            continue
        elif type(i) == float: # check if a floating number entered.
            print("You entered a floating number. Please try again.")
            continue
        elif type(i) == int and i < 0: # check if a negative integer entered.
            print("You entered a negative integer. Please try again.") 
            continue
        # max of 2 digit numbers allowed to prevent program crashing when large numbers entered.   
        elif type(i) == int and i >= 100: # check if a positive integer with more than 2 digits entered.
            print("You entered a positive integer but more than 2 digits.")
            print("You are only allowed max of 2 digits. Please try again.")
        else:
            # a positive integer with less than 3 digits entered.
            print("The sum is", sum(range(i+1))) # add numbers from 0 upto the number entered.
            break

    except: 
    # an unacceptable value detected.
        print("this is not a positive integer nor a string. Please try again")