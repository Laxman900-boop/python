Games = [] 

while True:
    game = input("Enter your favorite game: ")  
    if game == "":  
       Games.append(game)  

                  print("\nYour favorite games are:")
                           for game in Games:  
    print(game)
