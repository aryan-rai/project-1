import random

flag = true
while flag :
    num = input('Type a number for lower bound: ')

    if num.isdigit():
        print("Lets play!")
        num = int(num)
        flag = False
        else:
            print('Inavild input try again!')
            secret = random.randit(1.num)
            gues = None 
            count = 1
            while guess != secret :
                guess = input('Please type a number between 1 and ' + str(num) + ": ")
                if guess.isdidgit():
                    guess = int(guess)

                    if guess == secret :
                        print('You got it!')
                        else:
                            print('Wrong! Please try again!')
                            count += 1
                            print('You did it!', count, 'guesses!')