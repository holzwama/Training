import random

number = random.randint(1, 9)

player_name = input("Enter your Username")
print("The User: " + player_name + " has 10 tries")

def game():
    tries = 0
    while tries <= 10:
        
        print("Start guessing. This is guess: " ,tries)
        user_guess = int(input())
        if user_guess < number:
            print("The number to guess is higher!")
            tries += 1
        if user_guess > number:
            print("The number to guess is lower!")
            tries += 1    
        if user_guess == number:
            print("You guessed it right!")
            break
game()

