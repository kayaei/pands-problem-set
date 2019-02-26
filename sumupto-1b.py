# Etem Kaya 22-Feb-2019
# Solution-1b: Problem-1 second solution - "sumupto-1b.py".
"""
Problem-1: Write a program that asks the user to input 
any positive integer less than 100 and outputs the 
sum of all numbers between one and that number.
"""

while True:
# execute the code until a positive integer with less than 3 digit entered.
    try:
        i = int(input("Please enter a positive integer less than 100: "))

        # max of 2 digit numbers allowed to prevent program crashing when large numbers entered. 
        if 0 <= i < 100: # check if a positive integer with less than 3 digits entered.
            print("The sum is", sum(range(i+1))) # add numbers from 0 upto the number entered.
            break
        else:
            # number entered is outside the allowed range.
            print("A positive integer but greater than 99 or a negative integer entered, please try again.")
            continue

    except:
    # an unacceptable value detected.
        print("this is not a positive integer number, please try again.")