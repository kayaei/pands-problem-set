# Etem Kaya 15-Mar-2019

# Solution to Problem-9.
# File name: "second.py".

# Problem-9: Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.

# first import sys library.
import sys

# raise error if file doesn't exist or wrong filename supplied.
try:
    # count the number of arguments supplied via command-line
    if len(sys.argv) == 2: # sys.argv is a list contains commandline arguments.
        # open a text file in read only mode, which the filename _
        # is supplied from an argument on the command line.
        with open(sys.argv[1], 'r') as f:

            # assign the lines of the text file to a variable.
            s = f.readlines()

            # starting from line zero, loop through the every second line of_
            # the file (increment by 2) so lines 0, 2, 4, 6, etc.
            for i in range(0, len(s), 2):

                # print every second line of the file starting from line zero_
                # but ignore the empty lines e.g. 1, 3, 5, 7 etc.
                print(s[i], end='')
            # no need to close the file as it was opened in a 'with' statement.
            print ("\n \nFile is now closed.")
    # if sys function has less than or more than 2 elements.             
    else:
        print ("You should supply a single text file.")
        sys.exit()
# error detection on file errors e.g. file doesn't exist or wrong filename or_
# file extension is not valid or corruption where file cant be read etc.
except OSError:
    print("File error. Cann't open the file. Check the filename again.")