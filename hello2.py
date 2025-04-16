def conversation():
    print("Laxman: Hey Ram! How's it going?")
    ram_response = input("Ram: I'm doing well, thanks! How about you? ")

    print("Laxman: I'm good too! Just enjoying the day.")
    
    favorite_color = input("Laxman: By the way, what's your favorite color? ")
    print(f"Ram: Oh, I really like {favorite_color}! It's such a nice color.")

    location = input("Laxman: Nice! Where do you live these days? ")
    print(f"Ram: I live in {location}. It's a great place to be!")

    hobbies = input("Laxman: What do you like to do in your free time? ")
    print(f"Ram: I love {hobbies}. It really helps me unwind!")

    print("Laxman: Sounds awesome! It was great catching up with you, Ram!")
    print("Ram: Yeah, it was! Let's do this again soon.")

# Call the function
conversation()
