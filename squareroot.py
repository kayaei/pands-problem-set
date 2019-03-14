# Etem Kaya 13-Mar-2019

# Solution to Problem-7.
# File name: "squareroot.py".

# Problem-7: Write a program that that takes a positive floating point number
# as input and outputs an approximation of its square root.


# The number to calculate the square root of.
rootof = float(input("Enter a positive floating number to calculate square root of: "))

# The initial estimate for the square root.
estimate = float(input("Enter an initial estimate for square root: "))

# Keep calculating until the estimate is within 0.1 of rootof.
while abs((estimate * estimate) - rootof) > 0.1:
    # This is Neweton's method to improve the estimate.
    # Adapted from: https://tour.golang.org/flowcontrol/8
    estimate -= ((estimate * estimate) - rootof) / (2 * estimate)

# Print the result.
print(f"The square root of {rootof} is approx. {estimate}.")