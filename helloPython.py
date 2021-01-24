
from random import randint
secret_num = randint(1,100)
guess = 0
i=0
while i < 11:
    i+=1
    guess = int(input('Guess the secret number: '))
    if guess > secret_num:
        print("Your guess is higher than the number.")
    elif guess < secret_num:
        print("Your guess is lower than the number.")
    elif guess == secret_num:
        print("You finally got it!")
        break
    # else:
    #     print('You lost your 10 chances')
    if i==10 and guess!=secret_num:
        print('You lost your 10 chances')


# need random number generator between 1 and 100


# need to keep track of number of times user is guessing 


# while user guess is not equal to random guess and number of times user has is less than 10 continue


# if user guess is higher than random guess then print “higher” and display remaining number of times


# if user guess is lower than random guess then print “lower” and display remaining number of times 


# else print “congrats, you guessed the random number”



