
user_numbers = set()

print("Enter 7 unique numbers for the lottery:")
while len(user_numbers) < 7:
    try:
        num = int(input(f"Enter number {len(user_numbers) + 1}: "))
        if num in user_numbers:
            print("Error: This number is already in the set. Try a different number.")
        else:
            user_numbers.add(num)
    except ValueError:
        print("Error: Please enter a valid integer.")

print("\nYour lottery numbers are:", user_numbers)

winning_numbers = {10, 25, 32, 41, 43, 45, 50}

correct_numbers = user_numbers.intersection(winning_numbers)
num_correct = len(correct_numbers)

print(f"\nThe winning numbers are: {winning_numbers}")
print(f"You matched {num_correct} numbers: {correct_numbers}")

if num_correct == 3:
    print("You win 4$!")
elif num_correct == 4:
    print("You win 15$!")
elif num_correct == 5:
    print("You win 200$!")
elif num_correct == 6:
    print("You win 3000$!")
elif num_correct == 7:
    print("You win 5 000 000$!")
else:
    print("Sorry, you didn't win a prize. Better luck next time!")
