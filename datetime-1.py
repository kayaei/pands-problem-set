# Etem Kaya 15-Mar-2019

# Solution to Problem-8.
# File name: "datetime.py".

# Problem-8: Write a program that outputs today’s date and time in the format
# ”Monday, January 10th 2019 at 1:15pm”.

# import datetime module to check the current date.
import datetime as dt

# read the today's full date and time
t_day = dt.datetime.today()
# 'day of month' variable to read day of the month only as integer
d_month = int(t_day.strftime("%d"))
# setup the suffix for the day depending of the day of the month
if d_month in (1, 21, 31):
    d_suffix = 'st'
elif d_month in (2, 22):
    d_suffix = 'nd'
elif d_month in (3, 23):
    d_suffix = 'rd'
else:
    d_suffix = 'th'
 
# print current date and time in the format of "Monday, January 10th 2019 at 1:15pm". 
print((t_day.strftime("%A, %B %d"))+d_suffix,(t_day.today().strftime("%Y at %I:%M%p")))