# Etem Kaya 03-Mar-2019

# Solution-1b to Problem-4.
# File name: "divisors.py".

# Problem-4: Write a program that asks the user to input any positive integer
# and outputs the successive values of the following calculation. At each step
# calculate the next value by taking the current value and, if it is even,
# divide it by two, but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.

def collatz(n):
    print(n, end=' ')
    while n > 1:
        if  n % 2 == 0: # when user input is an even number.
            n = n//2 # set next user input number automatically.
            print(n, end=' ')
            
        elif  n % 2 != 0: # when user input is an odd number.
            n = (n * 3) + 1 # set next user input number automatically.
            print(n, end=' ')

while True:
    try: 
        n = int(input("Please enter a positive integer: "))    
        if n == 1:
            print("Your Input is already 1.")
            break
    except ValueError: 
        print("This is unaccaptable value. Run it again")
        continue
    else:
        print("Your Collatz Sequence is")
        break

collatz(n)