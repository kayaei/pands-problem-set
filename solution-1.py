# Solutions to problem 1

x = int(input("Please enter a positive integer: "))
if x < 0:
    print('That is a negative integer. Please enter a positive integer')
else:
    print(sum(range(1,x+1)))
