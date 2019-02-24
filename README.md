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
The followings Loops, Blocks and Statements are used;
1. 'While' loop with 'continue' and 'break' statements: I started with a 'While' loop with 'continue' and 'break' statement, because I wanted to loop back to top of the code and will continue asking a positive integer. Since the 'True' always evaluates to True, my 'While' loop will run indefinetely so keep asking a positive integer until one less than 99 is entered. I also limited the max entry for the positive integer number to 99, because in case a very large positive integer number is entered (e.g. 123456789123456789), which can increase the load on the CPU and can lead system crashes. I also used the 'continue' and 'break' statements in my 'While' loop. So with the 'continue' statement, I don't execute the rest of the code and instead go back to the 'While' loop at the top of my code and keep asking a positive integer number. This will repeat indefinetely until a positive integer number is entered which will be caught by the 'break' statement. So the 'break' statement breaks the 'While' loop when there is a match as in a positive integer less than 99 is entered so unlike the 'continue' statement which will loop back to the top of the code, the 'break' statement will stop or break the loop when a match is found (a positive integer les than 99 is entered).     

2. 'try' and 'except' Block: I used the 'try' and 'except' statements to catch and handle any exceptions with the 'While' loop so any any entries that don't form a proper numbers or strrings such as 1,33 instead of 1.33 or abcdef or @&^%%$£ with no quotes around. The code runs as normal following the 'try' statement and if an exception is detected, the response to that exception is handle after the 'except' statement, which might be generally displaying an eror message. Since my 'try' and 'except' block is within the 'While' loop, aas soon as the exception is handled after the 'except' statement, it goes back to the 'while' loop at the top and keep asking a positive integer number again. This will repeat until a positive number is entered so that the loop is broken at the 'break' statement.   
3. 'eval', 'input', 'print', 'sum' and 'range' functions: I used 'eval' with 'input' funtions to evaluate the value entered wheter it is a stringor a negative integer or a floatign number or a positive integer with more than 2 digits etc.. With the 'print' statement, the resilt is dipalyed on the screen. The 'sum' with 'range' funtions wrapper together 'sum(range(i+1))' gives me the sum of the numbers from zero upto the number entered save me a few lines of code so I dont have to use another 'while' loop or a 'for' loop with another variable to calculate the sum. 
4. 'if', 'elif' and 'else' statements: Like any other programming languages, the 'if' and 'else' statements are very similair and used to evaluate a condition being true or false. So I used them to evaluate the type of values entered. The 'elif' statement saved me a few lines of code so instead of having multiple 'if' statements nestes and each one witt its own 'else' statement, I used 'elif' statements and reduced the lines of code and yet achived the same result so shorten my code.

#### File Name: 
1. sumupto-1a.py

#### References:
1. https://docs.python.org/3/tutorial/errors.html#handling-exceptions 
2. https://docs.python.org/3/tutorial/controlflow.html#if-statements 
3. https://www.quora.com/How-do-you-check-if-a-number-is-a-float-in-Python 
4. https://www.youtube.com/watch?v=jlOyXjfxEOs 
