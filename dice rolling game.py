import random
print("Welcome to Dice world")
while True:
    choice = input("Press 1 to play\nPress 2 to exit")
    if choice == '2':
        print("User Quit")
        break
    elif choice == '1':
        num = random.randint(1,6)
        print("You have",num,"in your dice!!")
    else:
        print("Invalid Input by user!!")
        print("Game over")
        break
