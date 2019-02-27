# Etem Kaya 26-Feb-2019
# Solution-2: Problem-2 solution - "begins-with-t.py".
"""
Problem-2: Write a program that outputs whether or not today is a day that begins with the
letter T. An example of running this program on a Thursday is "Yes - today begins with a T.".
An example of running it on a Wednesday is "No - today does not begin with a T.".
"""

import datetime # import the datetime module to get the current date.

# set up a curent day variable using the datetime module. 
Tday = datetime.datetime.today().strftime("%a") # convert the value of the current day varibale into a short version weekday string.
if  Tday[0] == "T": # check if the current day variable starts with letter "T" (check if the first element of current day string is "T").
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.")