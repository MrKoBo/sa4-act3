number = 10
guesses = 5

print("I'm thinking of a number...")
correct = False
guess = input(f"You have {guesses} guesses. What number am I thinking of? (If you give up press q) ")
while not correct and guess != 'q':
    
    if guess != "q":
        guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break

    elif guesses > 0:
        guesses -= 1
        if guess > number:
            guess = input(f"Sorry, your guess was too high, you have {guesses} guess(es) remaining try again! ")
        else:
            guess = input(f"Sorry, your guess was too low, you have {guesses} guess(es) remaining try again! ")
    if guesses == 0:
        print(f"Sorry the correct answer was {number} you have ran out of guesses.")
        break


else:
    
    print(f"Sorry, the correct answer was {number}")