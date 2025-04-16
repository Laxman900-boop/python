import random

my_number = random.randint(0, 100)
 

while True:
    try: 
        guess = int(input("Guess a number between 0 and 100: ")) 

        if guess > my_number:
            print("It is too high, try again.")
        elif guess < my_number:
            print("It is too low, try again.")
        else:
            print("Huge congratulations! You guessed the correct number.")
            break  

    except ValueError:
        print("Invalid input! Please enter a valid number.")
