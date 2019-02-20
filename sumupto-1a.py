# Solution to problem 1

while True:
  try:
    # evaluate the value entered.
    i = eval(input("Please enter a positive integer: "))

    if type(i) == str: # check a string entered.
      print("You entered a string. Please try again.")
      continue
    elif type(i) == float: # check a floating number entered.
      print("You entered a floating number. Please try again.")
      continue
    elif type(i) == int and i < 0: # check a negative integer entered.
      print("You entered a negative integer. Please try again.") 
      continue   
    elif type(i) == int and i >= 100: # check a positive integer with more than 2 digits entered.
      print("You entered a positive integer but more than 2 digits.")
      print("You are only allowed max of 2 digits. Please try again.")
    else:
      print("The sum is", sum(range(i+1))) # sum up numbers from 0 to the number entered.
      break  
  except:
    # Failure due to an unexpected value entered.
    print("Opps, this is an unacceptable value. Please try again")