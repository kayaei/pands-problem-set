# Etem Kaya 16-Mar-2019

# Solution to Problem-10.
# File name: "plotfunction.py".

# Problem-10: Write a program that displays a plot of the functions x, x2 & 2x
# in the range [0, 4].

#Import matplotlib and numpy packages 
import matplotlib.pyplot as plt
import numpy as np

# setup the lenght and scale of the x axis
# plt.axis([0, 4, 0, 15])
x = np.arange(0.0, 4.0, 0.5)

# define the functions y1, y2 and y3 
y1 = x         # f(x) function
y2 = x**2      # f(x**2) function            
y3 = 2**x      # f(2**x) function

## plot the y1, y2 and y3 functions
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

# pionts where the y1, y2 and y3 functions intersect and_
# mark the point where they intersect with orange and blue colours
plt.plot(1, 1, 'or')
plt.plot(2, 4, 'bo')

## Config the graph
plt.title('Plotting Graph for functions f(x), f(x^2) and f(2^x)')
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')

# turnon grid lines visibility
plt.grid(True)

# setup plot legends for each line and their locations for display
plt.legend(['y1 = x', 'y2 = x^2', 'y3 = 2^x'], loc='upper left')

## plot the y1, y2 and y3 functions on the graph
plt.show()
