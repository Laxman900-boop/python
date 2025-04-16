total = 0
while True:
    try:
           number = int(input("enter your number (enter 0 to exit)\n"))
    if number == 0:
         break
    else:
        total += number
    except ValueError:
print("invalid, please enter only numbers")