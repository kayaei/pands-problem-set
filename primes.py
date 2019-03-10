# Etem Kaya 10-Mar-2019

# Solution to Problem-5.
# File name: "primes.py".

# Problem-5: Write a program that asks the user to input a positive integer
# and tells the user whether or not the number is a prime.

# promt user to input a positive integer number.
n = int(input("Please enter a positive integer: "))

# import math function
import math

# define a function to check user input is prime or not.
def prime(n): 
    # any integer < 2 not prime
    if n < 2: 
        print(n, "is not a prime.")  
        return
    # use math and square root with round down functions to find_
    # possible number of divisors for the given input n.
    divisors = math.floor(math.sqrt(n))

    # loop to check only odd numbers from 3 up to the floor of square root of n.
    for x in range(2, divisors + 1):
        # odd number and > 2 but has divisors other than 1 and self.
        if n % x == 0:   
            print(n, "is not a prime.")
            break # terminate the loop.
    # odd number and > 2, and no divisors other than 1 and self.
    else:
        print(n, "is a prime.")

# call the funtion
prime(n)