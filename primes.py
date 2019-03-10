# Etem Kaya 10-Mar-2019

# Solution to Problem-5.
# File name: "primes.py".

# Problem-5: Write a program that asks the user to input a positive integer
# and tells the user whether or not the number is a prime.

# import math function
import math

# define a function to check user input is prime or not.
def prime(n): 
    # integers < 2 not prime
    if n < 2: 
        print(n, "is not a prime.")  
    # integers 2 is already prime.
    if n == 2:   
        print(n, "is a prime.")
    # all even numbers which are > 2 are not prime.
    if n > 2 and n % 2 == 0:   
        print(n, "is not a prime.")

    # use math and square root with round down functions to find_
    # possible number of divisors for the given input n.
    divisors = math.floor(math.sqrt(n))

    # loop to check only odd numbers from 3 up to the square root of the input n.
    for x in range(3, divisors):
        # when it's even and > '2'.
        if n % x == 0:   
            print(n, "is not a prime.")
            break # terminate while loop.
    else:
        print(n, "is a prime.")

n = int(input("Please enter a positive integer: "))

# call the funtion
prime(n)