numbers = set()

while len(numbers) < 7:
    try:
        num = int(input("Enter a number: "))
        if num in numbers:
            print("You already entered that number. Try again.")
        else:
            numbers.add(num)
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Your numbers are:", numbers)


winning = {10, 25, 32, 41, 43, 45, 50}
print("Winning numbers are:", winning)

match = numbers & winning
print("You matched these numbers congratulations dude:", match)


count = len(match)

if count == 3:
    print("You won $4")
elif count == 4:
    print("You won $15")
elif count == 5:
    print("You won $200")
elif count == 6:
    print("You won $30000")
elif count == 7:
    print("You won $5,000,000")
else:
    print("No prize. Better luck next time!")
