# Etem Kaya 26-Feb-2019
# Solution-2: Problem-2 solution - "begins-with-t.py".
"""
Problem-2: Write a program that outputs whether or not today is a day that begins with the
letter T. An example of running this program on a Thursday is "Yes - today begins with a T.".
An example of running it on a Wednesday is "No - today does not begin with a T.".
"""

import datetime

if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3:
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.")