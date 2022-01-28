print("Welcome to Guess the Number Game")

while True:
    num = int(input("Enter the number between 1-10"))
    if num == 8:
        print("You win")
        # break
        choice = int(input("Press 1 to play more\nPress 2 to exit"))
        if choice == 2:
            break
    elif num > 8:
        print("Try smaller numbers")
    elif num < 8:
        print("Try some bigger number")