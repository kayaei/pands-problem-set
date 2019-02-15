# Solutions to problem 1

try:
    i = int(input("Please enter a positive integer: "))
    if i < 0:
        print("That is not a positive integer. Please try agaion")
    else:
        print(sum(range(i+1)))
except ValueError:
    print("This is not an integer. Please try again") 
