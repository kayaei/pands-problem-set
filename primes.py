# Etem Kaya 10-Mar-2019

# Solution to Problem-5.
# File name: "primes.py".

# Problem-5: Write a program that asks the user to input a positive integer
# and tells the user whether or not the number is a prime.

while True: # alway true until it breaks with user input.
    # try-except block to catch if no integer entered.
    try: 
        n = int(input("Please enter a positive integer: "))
        # when it's < 2.
        if n < 2: 
            print(n, "is not a prime. Try again.") 
            continue # keep asking until user enters an integer >= 2           
    # an error detected when a non-integer value entered.
    except ValueError: 
        print("You entered a non-integer value. Try again.")
    # when it's >= 2.
    else:
        # when it's '2'.
        if n == 2:   
            print(n, "is a prime.")
            break # terminate while loop.
        while n > 2:
            for x in range(3, n+1):
                # when it's even and > '2'.
                if n % x == 0:   
                    print(n, "is not a prime.")
                    break # terminate while loop.
            else:
                print(n, "is a prime.")
                break # terminate while loop.
    break # terminate while loop.