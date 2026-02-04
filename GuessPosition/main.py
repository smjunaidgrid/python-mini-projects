# Match the Location through user CLI input
from random import shuffle

mylist = [' ','O',' ']

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
            guess = input("Guess the position 0,1,2 : ")
    return int(guess)

shuffle_list(mylist)

while True:
    guess = player_guess()
    if mylist[guess]=='O':
        print("Guessed Correctly!")
        print(mylist)
        break
    else:
        print("Wrong guess..try again..")
    
