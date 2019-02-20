while True:
    try:
        # limit entries to integer numbers only.
        i = int(input("Please enter a positive integer less than 100: "))
         
        if 0 <= i < 100: # check if a positive integer less than 100 entered.
            print("The sum is", sum(range(i+1))) # sum up numbers from zero to the number entered.
            break
        else:
            print("An integer less than 0 or greater than 99 entered, please try again.")
            continue 
    except:
        print("False entry, please try again.")