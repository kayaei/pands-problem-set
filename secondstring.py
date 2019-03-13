# Etem Kaya 11-Mar-2019

# Solution to Problem-6.
# File name: "secondstring.py".

# Problem-6: Write a program that takes a user input string and outputs every second word.

My_sentence = "this is a funny cheese shop but there is no mice in this shop"
# print(text.partition(' '))[2] # cheese shop
My_sentence = My_sentence.split()[::2]
print(My_sentence)
