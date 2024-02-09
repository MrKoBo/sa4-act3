number = 10
guesses = 5

print("I'm thinking of a number...")
correct = False
guess = input(f"You have {guesses} guesses. What number am I thinking of? (If you give up press q) ")
guesses -= 1
while not correct and guess != 'q':
    
    if guess != "q":
        guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guesses > 0:
        guess = input(f"Uh oh! you now have {guesses} many guesses left. Try again! ")
        guesses -= 1
    if guesses == 0:
        print(f"Sorry the correct answer was {number} you have ran out of guesses.")
        break
else:
    
    print(f"Sorry, the correct answer was {number}")