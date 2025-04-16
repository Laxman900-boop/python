correct_password = "5555"
attempt = 0
max_attempt = 3
input_password = ""
balance = 500.0  

while attempt < max_attempt and input_password != correct_password:
    input_password = input("Enter your password:")
    
    if input_password == correct_password:
        while True:
            print("Choose an option:")
            print("1. Deposit") 
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")
            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                amount = input("Enter amount to deposit: $")
                
                amount = float(amount)
                if amount > 0:
                        balance += amount
                        print(f"### Deposited successfully. New balance: ${balance:.2f}\n")
                else:
                        print("### Error: Deposit amount must be greater than zero.\n")
               

            elif choice == "2":
                amount = input("Enter amount to withdraw: $")
                
                amount = float(amount)
                if amount <= balance:
                        balance -= amount
                        print(f"### Withdrawn successfully. New balance: ${balance}\n")
                else:
                        print("### Error: Insufficient funds.\n")
                

            elif choice == "3":
                print(f"### Current Balance: ${balance}\n")

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("### Error: Invalid option. Please try again.\n")
    else:
        attempt += 1
        print(f"Incorrect PIN. You have {max_attempt - attempt} attempt(s) left.")

        if attempt == max_attempt:
            print("Too many attempts. Your account is blocked.")