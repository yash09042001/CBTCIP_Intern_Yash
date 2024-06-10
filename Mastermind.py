import random

num = random.randrange(1000, 10000)
print(num)
chances = 5
guess = int(input(f'Guess a 4 digit number, you have {chances} chaneces left: '))
if guess == num:
    print('Great you won, now you are a mastermind')
else:
    tries = 0
    while guess != num and chances:
        tries += 1
        chances -= 1
        rigthdigits = 0
        guess = str(guess)
        num = str(num)
        correct = ['X'] * 4
        for i in range(0, 4):
            if guess[i] == num[i]:
                rigthdigits += 1
                correct[i] = num[i]
        if rigthdigits < 4 and rigthdigits > 0 and chances:
            print('Not the right guess, but you guessed', rigthdigits, 'numbers rigth')
            print('Current status is:')
            for char in correct:
                print(char, end=' ')
            print('\n')
            print('\n')
            guess = int(input(f'Guess a 4 digit number, you have {chances} chaneces left: '))
        elif rigthdigits == 0 and chances:
            print('none of the digits you guessed is right')
            guess = int(input(f'Guess a 4 digit number, you have {chances} chaneces left: '))
    if guess == num:
        print('Great you won in', tries, 'guessed, now you are a mastermind')
    if chances == 0:
        print('Sorry, you lost, as you ran out of chances')
        print('number is ', num)
