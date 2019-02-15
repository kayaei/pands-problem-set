# Solutions to problem 1

while True:
  try:
    i = eval(input("Please enter a positive integer: "))

    if type(i) == str:
      print("You entered a string. Please try again")
      continue
    elif type(i) == float:
      print("You entered a floating number. Please try again")
      continue
    elif type(i) == int and i < 0:
      print("You entered a negative integer. Please try again") 
      continue   
    else:
      # Success. You entered a positve integer.
      print("The sum is", sum(range(i+1)))
      break  
  except  ValueError:
    # You did not enter a proper string or number. 
    print("This is not an integer number at all. Please trey again")
