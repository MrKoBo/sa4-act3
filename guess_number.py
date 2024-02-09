number = 10

print("I'm thinking of a number...")
correct = False
guess = input("What number am I thinking of? (If you give up press q) ")
while not correct and guess != 'q':
    
    if guess != "q":
        guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        guess = input("Sorry, that is not right try again! ")
else:
    
    print(f"Sorry, the correct answer was {number}")