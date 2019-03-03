# Etem Kaya 26-Feb-2019

# Solution to Problem-2.
# File name: "begins-with-t.py".

# Problem-2: Write a program that outputs whether or not today is a day that begins with the
# letter T. An example of running this program on a Thursday is "Yes - today begins with a T.".
# An example of running it on a Wednesday is "No - today does not begin with a T.".

# import datetime module to get the current date.
import datetime

# declare a variable and convert it to a short day string using the strftime function. 
Tday = datetime.datetime.today().strftime("%a")
# check if variable starts with letter "T" (first element is "T").
if  Tday[0] == "T": 
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.")