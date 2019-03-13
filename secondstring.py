# Etem Kaya 11-Mar-2019

# Solution to Problem-6.
# File name: "secondstring.py".

# Problem-6: Write a program that takes a user input string and outputs every second word.

My_sentence = str(input("Please enter a sentence: "))

# My_sentence = My_sentence.split()[::2]
# print(My_sentence)
# print(My_sentence.split()[::2])
# print(' '.join(My_sentence))
print(' '.join(My_sentence.split()[::2]))