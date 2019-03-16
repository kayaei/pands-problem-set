# Etem Kaya 15-Mar-2019

# Solution to Problem-9.
# File name: "dsecond.py".

# Problem-9: Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.


# open a text file containing first paragraph of Moby-Dick book in read-only mode.
text_file = open('C:\\Users\\etemk\\Desktop\\pands-problem-set\\moby-dick.txt', 'r')

# assign the lines of the text file to a new variable called 'lines'.
line = text_file.readlines()

# loop through every second line of the text file starting from line zero,
# then increment by 2 like 0, 2, 4, 6, etc.
for i in range(0, len(line), 2):
    
    # print every second line of the file starting from index zero.
    print (line[i])

# close the file.
text_file.close()
print("\n \nThe file is now closed. Goodbye.")