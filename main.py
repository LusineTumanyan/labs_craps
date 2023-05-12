
import random


def play_craps():
    roll = random.randint(1, 6) + random.randint(1, 6)

    if roll == 7 or roll == 11:
        print("You rolled: {}".format(roll))
        print("You win!")
    elif roll == 2 or roll == 3 or roll == 12:
        print("You rolled: {}".format(roll))
        print("You lose!")
    else:
        print("You rolled: {}".format(roll))
        goal = roll
        print("Roll again, Your goal is {}".format(goal))


        while roll:
            roll_again = input("Press Enter to roll again...")
            roll = random.randint(1, 6) + random.randint(1, 6)
            print("You rolled: {}".format(roll))

            if roll == 7:
                print("You lose!")
                break
            elif roll == goal:
                print("You win!")
                break
            else:
                roll = random.randint(1, 6) + random.randint(1, 6)
                print("You rolled: {}".format(roll))


play_craps()
