# Etem Kaya 15-Mar-2019

# Solution to Problem-9.
# File name: "dsecond.py".

# Problem-9: Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.


# open the text file containing first paragraph of Moby-Dick book in read-only mode.
f = open('C:\\Users\\etemk\\Desktop\\pands-problem-set\\moby-dick.txt', 'r')

# read the whole text file and display on the screen.
print(f.read())

# close the file.
f.close()
print("The file is now closed")