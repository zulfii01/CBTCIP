import random
while True:

    print("CHOSE BETWEEN \nEnter 0 for Rock \nEnter 1 for Paper \nEnter 2 for Scissors\nEnter 5 to end the game")
    user_choice = int(input("Enter your choice : "))

    d = {
        0: 'Rock',
        1: 'Paper',
        2: 'Scissors'
    }
    comp_choice = random.randint(0, 2)
    print(f"Computer chose ==> {d[comp_choice]}")

    if user_choice == comp_choice:
        print("OOPS!!!, Match draw\n")

    elif user_choice == 0 and comp_choice == 1:
        print("OOPS!!!, You LOST\n")

    elif user_choice == 1 and comp_choice == 2:
        print("OOPS!!!, You LOST\n")

    elif user_choice == 2 and comp_choice == 0:
        print("OOPS!!!, You LOST\n")

    elif user_choice == 0 and comp_choice == 2:
        print("Hurray!!!, You Won\n")

    elif user_choice == 1 and comp_choice == 0:
        print("Hurray!!!, You Won\n")

    elif user_choice == 2 and comp_choice == 1:
        print("Hurray!!!, You Won\n")

    elif user_choice == 5:
        break
    else:
        print("Invalid Input\n")


