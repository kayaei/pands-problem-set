# Etem Kaya 03-Mar-2019

# Solution to Problem-4.
# File name: "divisors.py".

# Problem-4: Write a program that asks the user to input any positive integer
# and outputs the successive values of the following calculation. At each step
# calculate the next value by taking the current value and, if it is even,
# divide it by two, but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.

def collatz(n): # define a function for collatz sequence.
    print(n, end=' ')
    while n > 1:
        # when user input is an even number.
        if  n % 2 == 0: 
            n = n//2 # calculate next input number automatically.
            print(n, end=' ')
            
        else:
            # when user input is an odd number.
            n = (n * 3) + 1 # calculate next input number.
            print(n, end=' ')

while True: # alway true loop until it breaks with user input.
    # try-except block to catch if no integer entered.
    try: 
        n = int(input("Please enter a positive integer: ")) 
        if n < 0: # a negative integer entered?
            print("You entered a negative integer. Try again.") 
            continue # keep asking until user to enter a positive integer.
        if n == 1: # Input '1' is not allowed due to '1, 4, 2' infinite cycle.  
            print("Opps, input '1' has '4,2,1' infinite cycle. Try again.")
            continue # keep asking until user to enter a positive integer.

    # an error detected as a non-integer value entered.
    except ValueError: 
        print("This is not an integer. Try again.")
    else:
        # Success, a positive integer greater than 1 entered.
        print("Your Collatz Sequence is;")
        break # terminate while loop and go to collazt function.

# call Collatz funtion
collatz(n) 