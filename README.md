# Problem Set 2019 - GMIT Data Analytics

#### Author: Etem Kaya ------------------------------------------------------------------- Project: Problem Set 2019
#### Institution: GMIT Ireland ------------------------------------------------------------ Course: Higher Diploma in Data Analytics
#### Module: Programming & Scripting ------------------------------------------------- Year and Semester: 2019 - 1
#### Date Released: 22-Feb-2019 --------------------------------------------------------- Software and Version: Python - Version 3.7

This repository contains my solutions to the Problem Set 2019 for the module "Programming and Scripting" at GMIT.

See this link for the instructions: (https://github.com/kayaei/pands-problem-set/blob/master/problems.pdf).

## How to download this repository

1. Go to GitHub.
2. Click the download button.

## How to run the code

1. You need to install Python first.

## Problems and Solutions

### Problem-1
Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one
and that number.

### Solution-1
In this solution I disallow certain characters to be entered. I also used the followings Loops, Blocks and Statements;
The ‘while’ loop: I started with a 'While' loop, because I wanted to loop back to the top of the code and continue asking a positive integer until it is achieved. Since 'True' always evaluates to True, my 'While' loop will run indefinitely and keeps asking a positive integer until one less than 99 is entered. I also limited my max entry for the positive integer number to 99, because in case user inputs a very large positive integer number (e.g. 123456789123456789), it can increase the load on the CPU and can lead to system crashes. I also used the 'continue' and 'break' statements. With 'continue', the rest of the code is not  executed, so it loops back to the top to the 'while' so it keeps asking a positive integer. This will repeat indefinitely until the loop breaks with a positive integer number less than 100. The 'break' statement stops the loop when a positive integer less than 100 is inputted.

The 'try' and 'except' block: I used it to catch and handle any exceptions such as any input that is not a positive integer less than 100 raises as error. The code runs as normal following the 'try' statement and if an exception is detected, the response to that exception is handled after the 'except' statement, which prints an error message. The code within the 'try-except' block is executed and user is asked to input a positive integer less than 100. This keeps repeating until the loop breaks at the 'break' statement when a number less than 100 is detected. The 'int', 'input', 'print', 'sum' and 'range' functions are also used. I used 'int' with 'input' functions to disallow certain characters, so restricting user to input integer numbers only. With the 'print' statement, the result is displayed on the screen. The 'sum' with 'range' functions wrapped together 'sum(range(i+1))' gives me the sum of all the numbers from zero up to the number entered. The 'if' and 'else' statements are also used to evaluate a condition being true or false.

#### File Name: 
1. sumupto.py

#### References:
1. https://docs.python.org/3/tutorial/errors.html#handling-exceptions
2. https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
3. https://docs.python.org/3/tutorial/controlflow.html#if-statements  
4. https://www.youtube.com/watch?v=jlOyXjfxEOs
5. https://realpython.com/python-exceptions/

### Problem-2
Write a program that outputs whether or not today is a day that begins with the letter T. An example of running this program on a Thursday is "Yes - today begins with a T.".

### Solution-2
I used Python’s datetime module to get the current day into a variable 'Tday'. The initial value in this varible was stored in long datetime format. I then converted this value into the short version of day format in string, so instead of full string like 'Tuesday', I stored it as 'Tue'. Following this conversion, I used the 'if' and 'else' statements to check the first element of this string to see it begans with the letter "T" or not, and depending on the result of this evaluation, I printed an appropriate message on the screen to say "Yes - today begins with a T." or "No - today does not begin with a T.".

#### File Name: 
1. begins-with-t.py

#### References:
1. https://docs.python.org/3/tutorial/stdlib.html#dates-and-times
2. https://docs.python.org/3/library/datetime.html
3. https://docs.python.org/3/library/datetime.html?highlight=strftime
4. https://stackoverflow.com/questions/7108080/python-get-the-first-character-of-the-first-string-in-a-list

### Problem-3
Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

### Solution-3
I used a simple 'for loop' with a range function to resolve the problem-3. In my for loop, I tested every number in my range from 1000 to 10000 to check if they csan be divisible by 6 but not 12 aty the same time. In the mean time, I counted every occurance that met the condition where the numbers in my range was divisible by 6 but not 12. The result was printed on the screen and with a final display to show the total occurrences where the above conditon was met. 

#### File Name: 
1. divisors.py

#### References:
1. https://docs.python.org/3/tutorial/controlflow.html#for-statements
2. https://docs.python.org/3/tutorial/controlflow.html#the-range-function

### Problem-4
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

### Solution-4
To resolve this problem, I used a number of statements, loops and functions which I learnt previously and used in my solutions to previous problems. These included 'int', 'input', 'print' along with two 'while' loops a 'try and except' block and a custom function.

First I first defined my custom function to calculate the collatz sequence based on the given creteria. I used a 'while' loop within my custom function with an 'if' and 'else' statements nested. 
Outdside my custom function 'collatz', I started with an alway true 'while' loop to eliminate inputs that are zero or negative integers which are not allowed for this collatz sequence. Within my alway true 'while' loop, I nested a 'try-except' block to detect errors when a non integer value entered. Within my 'try-except' block, I also used 'if', 'continue' and 'break' statements to check various scnerious and either continue or break the loop. Once all of the scnerious were tested and finally the predefined condition was met as user was alway forced to enter a positive integer number greater than '1', the always true 'while' loop was terminated with the 'break' statement and the custom function 'collatz' was called up to calculate the collatz numbering sequence based on the given input which met the predefined creteria (a positive integer greater than '1'). 

The reason why the integer '1' is not allowed in my collatz sequence is because the '1' results in the '4, 2, 1' infinate cycle which keeps repeating the same pattern forever. Besides, '1' is the destination number that we want to reach anyway. The number '0' is excluded from the sequence because it just returns itself '0' and we can never get to '1'. All negative integers are also excluded from this collatz numbering sequence in this given problem set.  

#### File Name: 
1. collatz.py

#### References:
1. https://docs.python.org/3/tutorial/controlflow.html#defining-functions
2. https://docs.python.org/3/tutorial/controlflow.html
3. https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming
4. https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
5. https://docs.python.org/3/tutorial/errors.html#handling-exceptions
6. https://stackoverflow.com/a/11758128

### Problem-5
Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.

### Solution-5
To resolve this problem, I used a 'for' loop with a custom 'function' I defined to execute the logic inside of it to check if user input is a prime number or not. I also imported the 'math' module with 'square-root' and 'floor' functions to round down the number. Overall, I used the 'int', 'input', 'print' and 'return' statements along with 2 'if' statements.
Firstly, I imported the 'math' module and used the 'square-root' and 'floor' functions later on in my custom function. Following that, I initiated a user input where user was asked to enter a positive integer number which was tested by the custom function whether the user input was a prime number or not. 
I defined my custom function called 'primes' to test if user inputs were prime or not. Once my custom function was defined, I called it at the bottom of my code. So within my function, I first eliminated any integers less than 2 as they are not prime numbers. Once I passed that test (user entered an integer either equal to 2 or greater than 2), I first declared a variable called 'divisors' using the math module and its 'square-root' and 'floor' functions to calculate the max number of possible divisors for a given input. This was particularly important because there is no need to check all numbers from 2 up to the user input itself to see if they are possible divisors for the user entered number. This square-root of the user input with rounding it down if not a whole number is a common rule in maths to say it is sufficient to check only numbers up to the square-root of that given integer (which may be rounded down if not a whole number).

I finally initiated a 'for' loop with an 'if' statement nested. This is where I tested those inputs equal or greater than 2, and the result was printed on the screen to indicate whether prime number or not.  

#### File Name: 
1. primes.py

#### References:
1. https://docs.python.org/3/tutorial/controlflow.html#defining-functions
2. https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
3. https://docs.python.org/3/tutorial/modules.html
4. https://docs.python.org/3/tutorial/controlflow.html#for-statements
5. https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
6. https://www.programiz.com/python-programming/examples/prime-number
7. https://beginnersbook.com/2018/01/python-program-check-prime-or-not/

### Problem-6
Write a program that takes a user input string and outputs every second word.

### Solution-6
To resolve this problem, I used the str.split() and str.join() functions of the string data type. First I got user to input a sentence, then I got this sentence split by every second word starting from the index zero. This means that the sentence is split by the elements that have the even index numbers like 0, 2, 4, 6 etc. So those elements with odd index numbers dropped from the list e.g. 1, 3, 5, etc. Then, these remaining words with even index numbers are joined to make a new sentence but a single space between each word as before and no single or double quotation around the words. And finally the result as in the new sentence was display on the screen.

I initialy started with a 'for' loop to check the lenght of the sentence and print only the even numbered words but that was more than 4 lines of code, where as this new solution is much shorter as i only use 2 lines of code with split and join both in a single line.  

#### File Name: 
1. secondstring.py

#### References:
1. https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
2. https://docs.python.org/3/tutorial/introduction.html#strings
3. https://docs.python.org/2.3/whatsnew/section-slices.html
4. https://www.programiz.com/python-programming/methods/string/join
5. https://stackoverflow.com/a/47085609
6. https://stackoverflow.com/a/12883445

### Problem-7
Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

### Solution-7
To resolve this problem, I started with a 'While' loop, because I wanted to loop back to the top of the code and continue asking to enter a positive floating-point number (inclusive of number zero). While 'True' is always True, my 'While' loop will run indefinitely and keeps asking a positive floating number until it is entered. I also used the 'continue' and 'break' statements within my While loop. 

With 'continue', the rest of the code is skipped, so it loops back to the top to the 'while True' and keeps asking a positive floating-point number. This will repeat indefinitely until the loop breaks when a positive floating-point number is entered so the result can be calculated. The 'break' statement stops the loop when the result is calculated and printed on the screen.    
After a value is entered by the user, with an if statement it is checked whether it is a negative number or not. If it is then a message is displayed on the screen to alert the user that this was a negative number so to try again so it loops back to the While True and will keep asking user to enter a positive floating number again. Once a positive number is entered (doesn't matter a float or an integer), it then asks user to enter a second number which is to be our initial estimate to calculate the square root of the first number entered. Once a second number is entered (negative number are permitted), it goes to another While loop to calculate the approx. square root of the first number entered. In this loop I used the Newton's square root approximation method which is widely available on the internet.   

Within my While True (always true) loop, I used the 'try-except' block to catch and handle any exceptions like input that is non numeric values like string or special characters etc. The code runs as normal following the 'try' statement and if an exception is detected (a non-numeric value is detected), the response to that exception is handled after the 'except' statement, which prints an error message. Then it goes back to the to the While True loop and executes the 'try-except' block again to ask user to input a positive number. This keeps repeating until the loop breaks at the 'break' statement when a number the result  (approx. square root) is calculated and displayed on the screen.
The goal of the Newton's square root approximation method is to calculate the approximate square root of the given number using the initial estimate given. There is also an accuracy constant of '0.01' used in the loop. This helps the accuracy of the square root as in how close we can get to the actual square root.

Note: Instead of Newton's square root approximation method, python's the built-in 'math.sqrt( x )' function can be used by importing the math module first ('import math').

#### File Name: 
1. squareroot.py

#### References:
1. https://tour.golang.org/flowcontrol/8
2. https://docs.python.org/3/tutorial/errors.html#handling-exceptions
3. https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming
4. https://docs.python.org/3/tutorial/controlflow.html#if-statements
5. https://stackoverflow.com/a/48438631
6. https://www.rookieslab.com/posts/finding-square-root-using-guess-and-check-algorithm-in-python

### Problem-8
Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.

### Solution-8
To resolve this problem, I first imported the 'datetime' module. Then I read today's full date and time into a variable called 't_day'. Subsequent to this, using the 'strftime' method from the 'datetime' module, I also read the 'day of the month' as integer into a new variable called 'd_month'. I then used this 'd_month' variable in my subsequent if and elif statements to determine what suffix I would need to add to the day of the month for display. So first I checked the day of the month and compared it against numbers in 3 tuples like (1, 21, 31) or (2, 22) or (3, 33) or the rest of the remaining days from a 31 day long calender month to find out where the day of the month was found. Depending on the result, one of these 4 possible string values ('st' or 'nd' or 'rd' or 'th') was asigned to a new variable called 'd_suffix' which was added after the day of the month when displayed on the screen.
I then converted today's date and time into the format requested and printed on the screen using the print function. With the 'strftime' method, I used the following legal codes;
1. %A = Weekday, long version, e.g. Wednesday
2. %B = Month name, long version, e.g. December
3. %d = Day of month (01-31), e.g. 31
4. %Y = Year, long version, e.g. 2018
5. %I = Hour 00-12 (12 hour clock), e.g. 05
6. %M = Minute 00-59, e.g. 41
7. %p = AM/PM, e.g. PM

Note: I had to change the file name from'datetime.py' to 'datetime-1.py' as my python interpretor didn't like the first name as it generated error for the datetime module saying that the 'datetime' module has no attribute 'datetime'. So I changed the file name with number 1 at the end to resolve the issue.

#### File Name: 
1. datetime-1.py

#### References:
1. https://www.w3schools.com/python/python_datetime.asp
2. https://docs.python.org/3/library/datetime.html
3. https://docs.python.org/3/tutorial/stdlib.html#dates-and-times
4. http://exponential.io/blog/2015/02/24/how-to-test-on-variable-against-multiple-values-in-python/

### Problem-9
Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.

### Solution-9
To resolve this problem, I imported the 'sys' library which I needed the 'sys.argv' function. Then I used a 'try and except' block to handle any file error exception by raising an error. To do that I used the 'OSError' except statement to catch any file errors such as wrong file name supplied or file not existed in the first place etc. Within the 'try-except' block, using an 'if' statement I first check the lenght of the argument supplied through the command-line and see the number of arguments (how many files) supplied. If 2 files supplied (a second file supplied through the command-line argument other than the python script file itself), then using the 'with' statement I accessed this second file as 'f'. Subsequent to this, using the file 'readlines' command, all of the lines of this file assigned to a variable called 's' so to use in my 'for' loop. I then initiated my 'for' loop to loop through numbers in a range with 3 step parameters;
start = index 0, which is the start with line zero in the file.
stop = 'len(s)' which is the total number of lines of the text file.
step = constant 2 is the jump between line so starting from line zero, jump to every second line like 0, 2, 4, 6, etc.).

Finally using the 'print' function, every second line was printed on the screen. In order to remove those empty lines (e.g. 1, 3, 5, etc.) between the every second lines, I used the end="" function to remove them. If however, there was no file supplied through the command-line argument other than the python script file itself, I then jumped to the else statement and using the 'print' function, I displayed a message for the user to indicate that a single text file (other than the python script file) to be supplied and ended the program.
Note: Because we used a 'with' function to access the file, we didn't need to close the file with the 'f.close()' command in our code as it was automatically closed at the end of the code when the result was achived and displayed on the screen.

#### File Name: 
1. second.py

#### References:
1. https://www.w3schools.com/python/python_file_open.asp
2. https://www.datacamp.com/community/tutorials/reading-writing-files-python
3. https://stackoverflow.com/q/22567785
4. https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
5. https://docs.python.org/3/library/sys.html?highlight=sys%20argv#sys.argv
6. https://www.pythonforbeginners.com/system/python-sys-argv

### Problem-10
Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

### Solution-10
To resolve this problem, I imported both 'numpy' and 'matplotlib' packages as they are very useful for plotting datasets. I first setup the scale and length of x axis using the 'arange' function of the numpy package (np.arange(0.0, 4.0, 0.5)). I then defined the following functions;
f(x) = y1 = x, 
f(x^2) = y2 = x^2, 
f(2^x) = y3 = 2^x. 
Using the 'plt' function of the 'matplotlib' package, I setup the plotting for those 3 functions. I also setup 2 pionts where these functions (y1, y2 and y3) will intersect and mark these point where they intersect with orange and blue colours. I turned on the grid line visibility to display both horizantal and vertical lines. I also setup the plot legends for each line and their locations purely for display purposes.
Finally, I plotted these f(x), f(x^2) and f(2^x) functions (y1, y2 and y3) on a single graph using the line chart where their intersect points marked blue and orange.

#### File Name: 
1. plotfunction.py

#### References:
1. https://matplotlib.org/users/pyplot_tutorial.html
2. http://courses.csail.mit.edu/6.867/wiki/images/3/3f/Plot-python.pdf
3. https://realpython.com/python-matplotlib-guide/
4. https://glowingpython.blogspot.com/2011/04/how-to-plot-function-using-matplotlib.html