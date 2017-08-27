import random
N=random.randint(0,9)
Num1 = input('Please enter the number of your choice: ')
NUMBER = int(Num1)
if NUMBER==N:
    print ("You guessed the perfect no")
elif NUMBER<N:
    print("You guessed the no less than the random no")
else:
    print("You guessed the no graeter than no")



