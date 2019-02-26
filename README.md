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

## Description of Problems and Solutions

### Problem-1

Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one
and that number.

### Solution-1a
I allow user to input anything first and then I do some sanity check on the input like evaluating what kind of value entered. I used the followings 'Loops, Blocks and Statements';
1. The 'while' loop: I started with a 'While' loop, because I wanted to loop back to the top of the code and continue asking a positive integer until it is achieved. Since 'True' always evaluates to True, my 'While' loop will run indefinitely and keeps asking a positive integer until one less than 99 is entered. I also limited my max entry for the positive integer number to 99, because in case user inputs a very large positive integer number (e.g. 123456789123456789), it can increase the load on the CPU and can lead to system crashes. I also used the 'continue' and 'break' statements. With 'continue', the rest of the code is not  executed, so it loops back to the top to the 'while' so it keeps asking a positive integer. This will repeat indefinitely until the loop breaks with a positive integer number less than 100. The 'break' statement stops the loop when a positive integer less than 100 is inputted.     

2. The 'try' - 'except' block: I also used a 'try' and 'except' statements to catch and handle any exceptions so any entries that don't form a proper numbers or strings such as 1,33 instead of 1.33 or abcdef or @&^%%$£ with no quotes around are raised as error. The code runs as normal following the 'try' statement and if an exception is detected, the response to that exception is handled after the 'except' statement, which generally prints an error message. When the 'try' and 'except' block is finished executing the code, which means the code in the 'while True' is finished executing, the code within the 'try-except' block is executed again so user is asked to input a positive integer less than 100 again. This keeps repeating until the loop breaks at the 'break' statement when a number less than 100 is detected.

3. The 'eval', 'input', 'print', 'sum' and 'range' functions: I used 'eval' with 'input' functions to evaluate the value entered whether it is a string or a negative integer or a floating number or a positive integer with more than 2 digits. With the 'print' statement, the result is displayed on the screen. The 'sum' with 'range' functions wrapped together 'sum(range(i+1))' gives me the sum of all the numbers from zero up to the number entered, which saves a few lines of code where we don't have to use another 'while' or a 'for' loop with another variable to calculate the sum.
 
4. The 'if', 'elif' and 'else' statements: Like most other programming languages, the 'if' and 'else' statements are very similar in the context and used to evaluate a condition being true or false. The 'elif' statement saved me a few lines of code so instead of having multiple 'if' statements nested each one with its own 'else' statement, I used 'elif' statements to shorten the code and yet achieved the same result.


#### File Name: 
1. sumupto-1a.py

#### References:
1. https://docs.python.org/3/tutorial/errors.html#handling-exceptions 
2. https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
3. https://docs.python.org/3/tutorial/controlflow.html#if-statements 
4. https://www.quora.com/How-do-you-check-if-a-number-is-a-float-in-Python 
5. https://www.youtube.com/watch?v=jlOyXjfxEOs 

### Solution-1b
This solution is a bit shorter. In this solution I disallow certain characters to be entered at a text prompt. I also used the followings Loops, Blocks and Statements;
1. The ‘while’ loop: I started with a 'While' loop, because I wanted to loop back to the top of the code and continue asking a positive integer until it is achieved. Since 'True' always evaluates to True, my 'While' loop will run indefinitely and keeps asking a positive integer until one less than 99 is entered. I also limited my max entry for the positive integer number to 99, because in case user inputs a very large positive integer number (e.g. 123456789123456789), it can increase the load on the CPU and can lead to system crashes. I also used the 'continue' and 'break' statements. With 'continue', the rest of the code is not  executed, so it loops back to the top to the 'while' so it keeps asking a positive integer. This will repeat indefinitely until the loop breaks with a positive integer number less than 100. The 'break' statement stops the loop when a positive integer less than 100 is inputted.     

2. The 'try' and 'except' block: I used it to catch and handle any exceptions so any input that is not a positive integer less than 100 raises as error. The code runs as normal following the 'try' statement and if an exception is detected, the response to that exception is handled after the 'except' statement, which generally prints an error message. When the 'try' and 'except' block is finished executing the code, which means the code in the 'while True' is finished executing, the code within the 'try-except' block is executed again and user is asked to input a positive integer less than 100 again. This keeps repeating until the loop breaks at the 'break' statement when a number less than 100 is detected.

3. The 'int', 'input', 'print', 'sum' and 'range' functions are also used. I used 'int' with 'input' functions to disallow certain characters at a text prompt, so restricting user to input integer numbers only. With the 'print' statement, the result is displayed on the screen. The 'sum' with 'range' functions wrapped together 'sum(range(i+1))' gives me the sum of all the numbers from zero up to the number entered, which saves a few lines of code where we don't have to use another 'while' or a 'for' loop with another variable to calculate the sum.
 
4. The 'if' and 'else' statements are also used. Like most other programming languages, the 'if' and 'else' statements are very similar in the context and used to evaluate a condition being true or false. Since it was a single ‘if’ and ‘else’ statement, I did not need to use ‘elif’ in this solution.

#### File Name: 
1. sumupto-1b.py

#### References:
1. https://docs.python.org/3/tutorial/errors.html#handling-exceptions 
2. https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
3. https://docs.python.org/3/tutorial/controlflow.html#if-statements  
4. https://www.youtube.com/watch?v=jlOyXjfxEOs
5. https://realpython.com/python-exceptions/

### Problem-2

Write a program that outputs whether or not today is a day that begins with the letter T. An example of running this program on a Thursday is "Yes - today begins with a T.".

### Solution-2
I used Pythopn's datetime function with 'if' and 'else' statements to resolve this problem.


#### File Name: 
1. begins-with-t.py

#### References:
1. https://docs.python.org/3/tutorial/stdlib.html#dates-and-times