# Etem Kaya 15-Mar-2019

# Solution to Problem-8.
# File name: "datetime.py".

# Problem-8: Write a program that outputs today’s date and time in the format
# ”Monday, January 10th 2019 at 1:15pm”.

# import datetime module to check the current date.
import datetime as dt

# print current date and time in the format of "Monday, January 10th 2019 at 1:15pm". 
print(dt.datetime.today().strftime("%A, %B %dth %Y at %I:%M%p"))