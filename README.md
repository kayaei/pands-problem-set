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

