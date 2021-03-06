# Etem Kaya 13-Mar-2019

# Solution to Problem-7.
# File name: "squareroot.py".

# Problem-7: Write a program that that takes a positive floating point number
# as input and outputs an approximation of its square root.

# Always true loop until the result is found.
while True:
    try:
        # The number to calculate the square root of.
        rootof = float(input("Enter a positive floating number to calculate its square root of: "))
        
        # check the number entered is a negative.
        if rootof < 0: 
            print("You entered a negative number. Try again.") 
            continue # keep asking until user to enter a positive integer.

        # The initial estimate for the square root.
        estimate = float(input("Enter a number as an initial estimate for the square root: "))

        # Keep calculating until the estimate is within 0.01 of rootof.
        while abs((estimate * estimate) - rootof) > 0.1:
            # This is Neweton's method to improve the estimate.
            # Adapted from: https://tour.golang.org/flowcontrol/8
            estimate -= ((estimate * estimate) - rootof) / (2 * estimate)

        # Print the result.
        print(f"The square root of {rootof} is approx. {estimate}.")
        break # terminate the loop

    # detect when no numeric value entered.
    except ValueError:
        print("This is not a floating point number. Try again")