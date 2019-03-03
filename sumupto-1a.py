# Etem Kaya 22-Feb-2019

# First solution to Problem-1 (Solution-1a)
# Fine name: "sumupto-1a.py".

# Problem-1: Write a program that asks the user to input 
# any positive integer less than 100 and outputs the 
# sum of all numbers between one and that number.

# execute the code until a positive integer with less than 3 digit entered.
while True: 
# execute code between try - except block and catch errors at except function.
    try:
        # declare user input varibale, evaluate it for type of data entered.
        i = eval(input("Please enter a positive integer less than 100: "))

        if type(i) == str: # check a string value entered.
            print("You entered a string. Please try again.")
            continue # go to while True and continue executing the code 
        elif type(i) == float: # check a floating number entered.
            print("You entered a floating number. Please try again.")
            continue # go to while True and continue executing the code
        elif type(i) == int and i < 0: # check a negative integer entered.
            print("You entered a negative integer. Please try again.") 
            continue # go to while True and continue executing the code
        # max 2 digits allowed to prevent crashes when large numbers entered.
        # check a positive integer more than 2 digits entered.   
        elif type(i) == int and i >= 100: 
            print("You entered a positive integer but more than 2 digits.")
            print("You are only allowed max of 2 digits. Please try again.")
        # when a positive integer with less than 3 digits entered.
        else:
            # add all numbers from 0 upto that number entered and display it.
            print("The sum is", sum(range(i+1))) 
            break # terminate the loop and end the program 
    
    # catch any errors that don't form proper numbers of strings.
    except: 
    # an unacceptable value detected.
        print("this is not a positive integer nor a string. Please try again")