print("Hello welcome to our game")
name = input("Please enter your name: ")
print("Welcome to our game" , name)
answer = input("Do you wan to play game with us? (y/n) ").lower()
if answer == "y":
    print("Okay let's start")
else:
    print("Okay see you next time ")
    quit()

print("You came to dead end and you have to change your directory which way would you go? (left / right) ")
answer = input("Make your choise: ").lower()
if answer == "left":
    print("You came to dead end and you lose!")
elif answer == "right":
    print("You came accross river what would you do? swim / walk ")
    answer = input("Make your choise: ")
    if answer == "swim":
        print("Well there was an aligator an it ate you and you died rest in peace ^_^")
    elif answer == "walk":
        print("You walked to much and ran out of water and died rest in peace")
    else:
        print("Wrong answer!!")
else:
    print("Wrong answer!!")