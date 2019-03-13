# Etem Kaya 11-Mar-2019

# Solution to Problem-6.
# File name: "secondstring.py".

# Problem-6: Write a program that takes a user input string and outputs every second word.

# get user to enter a sentence.
user_sentence = str(input("Please enter a sentence: "))

# split the user sentence by every second word starting from index zero.
# this means split by even index numbered elements like 0, 2, 4, 6 etc.
# and drop odd index numbered elements 1,3, 5, etc. from the list.
# finally join these even index numbered words with a single space between
# but no single or double quotation around and display them on the screen.
print(' '.join(user_sentence.split()[::2]))