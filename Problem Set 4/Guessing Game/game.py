import random


while True:
    try:
        max = int(input('Level: '))        
        number = random.randint(1, max)
        break
    except ValueError:
        pass



def take_guesses():
    while True:
        try:
            guess = int(input('Guess: '))
            if guess > number:
                print('Too large!')
                pass
            elif guess < number:
                print('Too small!')
                pass
            elif guess == number:
                print('Just right!')
                break
            else:
                pass
        except ValueError:
            pass

take_guesses()



