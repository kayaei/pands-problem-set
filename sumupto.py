# Etem Kaya 22-Feb-2019

# First solution to Problem-1 (Solution-1b)
# Fine name: "sumupto-1b.py".

# Problem-1: Write a program that asks the user to input 
# any positive integer less than 100 and outputs the 
# sum of all numbers between one and that number.

# execute the code until a positive integer with < than 3 digit entered.
while True:
    # execute the code and catch errors at except function.
    try:
        # variable which user to input positive integers to.
        i = int(input("Please enter a positive integer less than 100: "))

        # when very large numbers entered, system slows down or crashes.
        # allow max 2 digits to prevent system crashes.       
        if 0 <= i < 100: # check if a positive integer < 100 entered.
            
            # add all numbers from 0 upto the number entered and print the result
            print("The sum is", sum(range(i+1))) 
            break # terminate the loop to end the program.

        # when the number entered is outside the allowed range.
        else:
            print("You entered an integer outside the allowed range. Try again.")
            continue # go to while True and continue executing the code

    # raise errors (catch when not a positive integer entered).
    except:
        print("You entered a non-integer value. Try again.")