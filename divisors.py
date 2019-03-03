# Etem Kaya 03-Mar-2019

# Solution to Problem-3.
# File name: "divisors.py".

# Problem-3: Write a program that prints all numbers between
# 1,000 and 10,000 that are divisible by 6 but not 12.

# counter that counts occurance of numbers divisible by 6 but not 12.
x = 0
for num in range(1000, 10000):
    # check if number is divisible by 6 but not 12
    if num % 6 == 0 and num % 12 != 0:
        print(num, "is a number divisible by 6 but not 12")
        # increase the counter by 1 for every occurance meeting above condition.
        x = x + 1 # go back to the 'for' to test next number in the range.

# when all the numbers in the range tested.
else:
    # display the number of occurances that meet the above condition.
    print(x, "occurrences found")