right_answer = "Tokyo"
attempts = 0
while attempts < 5:
    answer = input("What is the capital city of japan")
    if answer.strip().capitalize() == right_answer:
        print("correct! you are well  done.")
        break
    else:
        print("wrong answer. try again.")
        attempts += 1
        if attempts == 5:
            print("you have used all the attempts. so the correct answer is Tokyo")
            
