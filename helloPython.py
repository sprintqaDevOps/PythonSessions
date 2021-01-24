
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