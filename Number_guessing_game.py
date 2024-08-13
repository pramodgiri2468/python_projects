#Import necessary library.
import random
import math

#Taking Inputs
lower=int(input("Enter Lower number: "))
upper=int(input("Enter Upper number: "))

#Generating random number between lower and upper.
a=random.randint(lower,upper)
total_chances=math.ceil(math.log(upper-lower +1, 2))
print("\n\tYou've only ",total_chances," chances to guess the number\n")

#Initialising the number of guesses.
count=0
flag = False

#for calculation of minimum number of guesses depends upon range
while count < total_chances:
    count+=1

    #taking guessing number as input
    guess=int(input("Guess a number: "))

    #condition testing
    if a==guess:
        print("Congratulations you did it in ",count," try")

        #Once guessed, loop will break
        flag=True
        break
    elif a>guess:
        print("You guessed too small!")
    elif a<guess:
        print("You Guessed too high!")

        #If Guessing is more than required guesses, then to display this output
if not flag:
    print("You've used all chances, the number is ",a)
    print("Better Luck Next Time!")