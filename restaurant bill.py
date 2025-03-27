print("Menu list")
print("Burger: $10 - press 1")
print("Pizza: $12 - press 2")
print("Sushi $15 - press 3")

user_choice = int(input("Please enter the menu number: "))
number_guests = int(input("Please enter the number of guests: "))

if user_choice == 1:
    total_price = number_guests * 10
elif user_choice == 2:
    total_price = number_guests * 12
elif user_choice == 3:
    total_price = number_guests * 15

print(f"The total without discount is ${total_price}")

if total_price >= 200:
    total_with_discount = total_price - total_price * 0.2
    print(f"Total with discount ${total_with_discount}")
elif total_price >= 100:
    total_with_discount = total_price - total_price * 0.1
    print(f"Total with discount ${total_with_discount}")