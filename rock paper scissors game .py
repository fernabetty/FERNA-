
import random

words = ["rock", "paper", "scissors"]
guessed_words = []


def play_game(words):
    print("*****%%%WELCOME TO ROCK, PAPER, & SCISSORS GAME%%%*****")
    print("You have to guess the three words either ROCK, PAPER, SCISSORS only")
    
    guess = input("GUESS THE WORD PLEASE: ").lower()
    guessed_words.append(guess)
    print(guessed_words)
    while True:
        secret_word = random.choice(words)
    
        if (guessed_words=='paper' and secret_word=='scissors'):
            print(f"You lose, i had {secret_word}")
            break
        elif (guessed_words=='scissors' and secret_word=='paper'):
            print(f"You win!! i had {secret_word}")
            break    
        elif (guessed_words=='scissors' and secret_word=='rock'):
            print(f"You lose!! i had {secret_word}")
            break
        elif (guessed_words=='rock' and secret_word=='sciccors'):
            print(f"You win!! i had {secret_word}") 
            break   
        elif (guessed_words=='rock' and secret_word=='paper'):
            print(f"You lose!!, i had {secret_word}")
            break
        elif (guessed_words=='paper' and secret_word=='rock'):
            print(f"You win!!, i had {secret_word}")
            break
        else:
            break          
        
        
        
        
play_game(words)
        #check for invalid input
   # if 