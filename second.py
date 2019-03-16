# Etem Kaya 15-Mar-2019

# Solution to Problem-9.
# File name: "second.py".

# Problem-9: Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.


# open a text file containing first paragraph of Moby-Dick book in read-only mode.
with open('C:\\Users\\etemk\\Desktop\\pands-problem-set\\moby-dick.txt', 'r') as f:

    # assign lines of the text file to a new variable called 'lines'.
    lines = f.readlines()

    # looping through the every second line of the text file, but start_
    # from line zero then increment by 2 so lines 0, 2, 4, 6, etc.
    for i in range(0, len(lines), 2):
        
        # print every second line of the file starting from line zero.
        print(lines[i], end='')

print("\n \nThe file is now closed. Goodbye.")