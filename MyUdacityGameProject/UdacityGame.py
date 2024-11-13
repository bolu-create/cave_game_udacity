import time
import random

# Story Game from Udacity


def open_files(file_path):
    file = open(file_path, "r", encoding="utf8")
    file1 = file.read()
    file.close()
    return file1

# Funtion to print Sentences


def print_sentences(sents):
    sents = sents.split('\n')
    for el in sents:
        print(el)
        time.sleep(0.5)

# Function to ask user how to continue 1 or 2


def user_input():
    while True:
        try:
            user_input = int(input("Enter 1 or 2: "))
            if user_input in (1, 2):
                break  # Exit the loop if the input is 1 or 2
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid number (1 or 2).")
    return user_input

# Funtion to ask user yes or no "y/n"


def end_or_not():
    while True:
        try:
            user_input = input("Enter y or n: ")
            if user_input in ("y", "n"):
                break  # Exit the loop if the input is 1 or 2
            else:
                print("Invalid input. Please enter y or n.")
        except ValueError:
            print("Invalid input. Please enter a valid number (y or n).")
    return user_input


# Game function
def game():

    globe = True
    while globe:

        # Sentences with  "x##100" placeholder
        start = open_files("start.txt")
        enter_no_sword = open_files("enter_no_sword.txt")
        enter_w_sword = open_files("enter_w_sword.txt")
        enter_cave = open_files("enter_cave.txt")
        enter_cave_again = open_files("enter_cave_again.txt")
        fight_sword = open_files("fight_sword.txt")
        run = open_files("run.txt")
        lose_game = open_files("lose_game.txt")
        decide = open_files("decide.txt")

        # Names of mythical monsters
        villain = [
            'gremlin', 'witch', 'wicked sherman', 'dragon',
            'troll', 'serpent', 'werewolf', 'vampire',
            'kraken', 'cyclops', 'gorgon', 'basilisk',
            'sphinx', 'Minotaur', 'Hydrahead'
        ]

        l_weapon = [
            "Dagger", "Shortsword", "Rapier", "Tanto",
            "Kunai", "Shuriken", "Boomerang", "Whip",
            "Nunchaku", "Baton"
        ]

        h_weapon = [
            "Sword", "Axe", "Mace", "Warhammer",
            "Halberd", "Flail", "Glaive", "Morningstar",
            "Greatsword", "Greataxe"
        ]

        # Function to replace placeholders with a random name
        def replace_placeholder(sentence, n1, n2, n3):
            sentence = sentence.replace("x##100", n1)
            sentence = sentence.replace("y##200", n2)
            sentence = sentence.replace("z##300", n3)
            return sentence

        # Randomly select a name from the list
        # vn == villain_name
        # lw == light_weapon
        # hw = heavy_weapon
        vn = random.choice(villain)
        lw = random.choice(l_weapon)
        hw = random.choice(h_weapon)

        # Replace placeholders in sentences with the random name
        start = replace_placeholder(start, vn, lw, hw)
        enter_no_sword = replace_placeholder(enter_no_sword, vn, lw, hw)
        enter_w_sword = replace_placeholder(enter_w_sword, vn, lw, hw)
        enter_cave = replace_placeholder(enter_cave, vn, lw, hw)
        enter_cave_again = replace_placeholder(enter_cave_again, vn, lw, hw)
        fight_sword = replace_placeholder(fight_sword, vn, lw, hw)
        lose_game = replace_placeholder(lose_game, vn, lw, hw)

        sword = 0  # variable for mythical weapnon in cave
        loop = True  # Value for loop continuation
        print_sentences(start)

        while loop:

            print_sentences(decide)

            # User would like to go in house or in cave?
            user_glb = user_input()

            # 1. Part 1

            # user goes in the house with no sword
            if user_glb == 1 and sword == 0:
                print_sentences(enter_no_sword)
                user = user_input()

                # user chooses to fight
                if user == 1:
                    print_sentences(lose_game)  # user
                    # user wants to play again? (y/n) start game or not
                    user = end_or_not()
                    if user == "y":
                        sword = 0
                        loop = False
                        # Change creature name
                    elif user == "n":
                        sword = 0
                        loop = False
                        globe = False

                # User chooses to run
                elif user == 2:
                    print_sentences(run)

            # 2. Part 2

            # User goes in the house with sword
            elif user_glb == 1 and sword == 1:
                print_sentences(enter_w_sword)

                # User chooses to fight
                user = user_input()
                if user == 1:
                    print_sentences(fight_sword)  # user wins
                    # user wants to play again? (y/n) start game or not
                    user = end_or_not()
                    if user == "y":
                        sword = 0
                        loop = False
                        # Change creature name
                    elif user == "n":
                        sword = 0
                        loop = False
                        globe = False

                # user runs
                elif user == 2:
                    print_sentences(run)
                    # user returns to the door and cave decision again

            # Cave Story

            # User chooses to enter cave no sword
            elif user_glb == 2 and sword == 0:
                print_sentences(enter_cave)
                sword = 1  # user picks sword
            # user enters cave despite having sword
            elif user_glb == 2 and sword == 1:
                print_sentences(enter_cave_again)


game()
