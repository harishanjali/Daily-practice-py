import random

#guess the random number game infinite times.
while True:
    random_num = random.randint(1,9)
    i = 0
    while i < 3:
        guessed_number = int(input('Guess the number: '))

        if(guessed_number == random_num):
            print('You guessed it correct')
            break
        else:
            if(guessed_number < random_num):
                print('The number you guessed it bit small')
            else:
                print('The number you guessed it bit larger')
        i += 1
    else:
        print('You lost the game')
    restart_game = input('Do want to play again:(yes/no): ')
    if(restart_game=='no'):
        break
print('Game over')