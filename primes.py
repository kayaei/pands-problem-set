# Etem Kaya 10-Mar-2019

# Solution to Problem-5.
# File name: "primes.py".

# Problem-5: Write a program that asks the user to input a positive integer
# and tells the user whether or not the number is a prime.

while True: # alway true loop until it breaks with user input.
    # try-except block to catch if no integer entered.
    try: 
        n = int(input("Please enter a positive integer: "))
        # when it's a negative integer.
        if n < 0: 
            print("You entered a negative integer. Try again.") 
            continue # keep asking until user enters an integer > 1.
        # when it's zero .
        if n == 0: 
            print("Number '0' is not a prime. Try again.") 
            continue # keep asking until user enters an integer > 1.
        # when it's '1'.
        if n == 1:   
            print("Number '1' is not a prime. Try again.")
            continue # keep asking until user enters an integer > 1.
    # an error detected when a non-integer value entered.
    except ValueError: 
        print("You entered a non-integer value. Try again.")
    # when it's >= 2.
    else:
        # when it's '2'.
        if n == 2:   
            print("Number '2' is a prime.")
            break # terminate while loop.
        # when it's even and > '2'.
        if n > 2 and n % 2 == 0:   
            print("Number 'n' is not a prime.")
            break # terminate while loop.
    # when it's odd and > '2'.
    print("Number 'n' is a prime.")
    break # terminate while loop.