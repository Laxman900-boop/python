first_num = float(input("your first_num"))
second_num = float(input("your second_num"))
operation = input("input your operation")

if (operation == "+"):
     answer = first_num + second_num

elif (operation == "-"):
     answer = first_num - second_num

elif (operation == "*"):
     answer = first_num * second_num

elif (operation == "/"):
     answer = first_num / second_num

print(f"{answer}")            