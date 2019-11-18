# The computer randomly generates either rock, paper, scissors, lizard or spock.
def random():
    import random
    return random.randint(0, 4)

def computerChoice():
    ranint = random()
    if ranint == 0:
        return "rock"
    elif ranint == 1:
        return "paper"
    elif ranint == 2:
        return "scissors"
    elif ranint == 3:
        return "lizard"
    else:
        return "spock"

# This function asks for and cleans the user input.
def clean(x):
    return x.lower().strip()

# Check whether user input is rock, paper or scissors.
def userDecision():
    choice = input("What would you like to choose: rock, paper, scissors, lizard or spock? Please type out the full word.")
    choice = clean(choice)

    if choice == "rock":
        return "rock"
    elif choice == "paper":
        return "paper"
    elif choice == "scissors":
        return "scissors"
    elif choice == "lizard":
        return "lizard"
    elif choice == "spock":
        return "spock"
    else:
        print("Sorry, I don't understand your response. Please try again.")
        return userDecision()

# This function plays the game.
def game():
    a = computerChoice()
    b = userDecision()
    # Compare the computer choice to the user choice and see who won.
    if a == b:
        print("You and the computer both chose " + b + ". Tie!")
    elif a == "rock":
        if b == "paper":
            print("The computer chose rock. You chose paper. Paper covers rock. You win!")
        elif b == "scissors":
            print("The computer chose rock. You chose scissors. Rock crushes scissors. The computer wins.")
        elif b == "lizard":
            print("The computer chose rock. You chose lizard. Rock crushes lizard. The computer wins.")
        else:
            print("The computer chose rock. You chose spock. Spock vaporizes rock. You win!")
    elif a == "paper":
        if b == "rock":
            print("The computer chose paper. You chose rock. Paper covers rock. The computer wins.")
        elif b == "scissors":
            print("The computer chose paper. You chose scissors. Scissors cut paper. You win!")
        elif b == "lizard":
            print("The computer chose paper. You chose lizard. Lizard eats paper. You win!")
        else:
            print("The computer chose paper. You chose spock. Paper disproves Spock. The computer wins.")
    elif a == "scissors":
        if b == "rock":
            print("The computer chose scissors. You chose rock. Rock crushes scissors. You win!")
        elif b == "paper":
            print("The computer chose scissors. You chose paper. Scissors cut paper. The computer wins.")
        elif b == "lizard":
            print("The computer chose scissors. You chose lizard. Scissors decapitate lizards. The computer wins.")
        else:
            print("The computer chose scissors. You chose spock. Spock smashes scissors. You win!")
    elif a == "lizard":
        if b == "rock":
            print("The computer chose lizard. You chose rock. Rock crushes lizard. You win!")
        elif b == "paper":
            print("The computer chose lizard. You chose paper. Lizard eats paper. The computer wins.")
        elif b == "scissors":
            print("The computer chose lizard. You chose scissors. Scissors decapitate lizards. You win!")
        else:
            print("The computer chose lizard. You chose spock. Lizard poisons Spock. The computer wins.")
    else:
        if b == "rock":
            print("The computer chose spock. You chose rock. Spock vaporizes rock. The computer wins.")
        elif b == "paper":
            print("The computer chose spock. You chose paper. Paper disproves Spock. You win!")
        elif b == "scissors":
            print("The computer chose spock. You chose scissors. Spock smashes scissors. The computer wins.")
        else:
            print("The computer chose spock. You chose lizard. Lizard poisons Spock. You win!")

# Run the game.
game()