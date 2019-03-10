# Etem Kaya 10-Mar-2019

# Solution to Problem-5.
# File name: "primes.py".

# Problem-5: Write a program that asks the user to input a positive integer
# and tells the user whether or not the number is a prime.

def prime(n): # define prime number function.
    if n < 2: 
        print(n, "is not a prime.")  
    if n == 2:   
        print(n, "is a prime.")
    # if even number and > 2
    if n > 2 and n % 2 == 0:   
        print(n, "is not a prime.")
        return # terminate while loop.

    for x in range(3, n):
        # when it's even and > '2'.
        if n % x == 0:   
            print(n, "is not a prime.")
            break # terminate while loop.
    else:
        print(n, "is a prime.")

n = int(input("Please enter a positive integer: "))

# call the funtion
prime(n)