import time
                import random

"""
start= "you find yourself standing in an open field , filled with grass and yellow wildflowers.\nRumor has it that a pirate is somewhere around here, and has been terrifying the nearby village.\nIn front of you is a house.\nTo your right is a dark cave.\nIn your hand you hold your trusty  (but not very effective) dagger.\n"

enter_no_sword= "You approach the door of the house.\nYou are about to knock when the door opens and out steps a pirate.\nEep! This is the pirate's house!\nYou feel a bit under-prepared for this, what with only having a tiny dagger.\nWould you like to (1) fught or (2) run away? "

enter_w_sword = "You approach the door of the house.\nYou are about to knock when the door opens and out steps a dragon.\nEep! This is the dragon's house!\nThe dragon attacks you!\nWould you like to (1) fight or (2) run away?"

enter_cave= "You peer cautiously into the cave.\nIt turnns out to  be only a very small cave.\nYour eye catches a gliint of metal behind a rock.\nYou have found the magical Sword of Ogorth!\nYou discard your silly old dagger and take the sword with you.\nYou walk back out to the field.\n"

enter_cave_again= "You peer cautiously into the cave.\nYou've been here before, and gotten all the good stuff. It's just an empty cave now.\nYou walk back out to the field.\n"

fight_sword= "As the dragon moves to attack , you unsheath your new sword.\nThe sword of Ogorth shines brightly in your hand as you brace yourself for the attack.\nBut the dragon takes one look at your shiny new toy and runs away!\nYou have rid the town of the dragon. You are victorious!\nWould you like play again? (y/n)"

run = "You run back into the field. Luckily you dont seem to have been followed.\n"

lose_game = "You do your best..\nbut your dagger is no match for the wicked fairie.\nYou have been defeated!\nWould you like play again? (y/n)"

decide = "Enter 1 to knock on the door of the house.\nEnter 2 to peer into the cave.\nwhat would you like to do?\n(please enter 1 or 2)"
"""
# Story Game from Udacity
"""
def open_files (file_path):
    file = open(file_path, "r", encoding="utf8")
    file1 = file.read()
    file.close()
    file1 = file1.split('\n')
    return file1
"""

def print_sentences(sents):
  
    sents= sents.split('\n')
    for el in sents:
        print (el)
        time.sleep(0.25)

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

#print_sentences(open_files('RunDontFight.txt'))
#x= open_files('RunDontFight.txt')
#print(x)

def game():

    globe= True
    while globe:

        # Sentences with placeholders
        start = "You find yourself standing in an open field , filled with grass and yellow wildflowers.\nRumor has it that a x##100 is somewhere around here, and has been terrifying the nearby village.\nIn front of you is a house.\nTo your right is a dark cave.\nIn your hand you hold your trusty  (but not very effective) dagger.\n"
        enter_no_sword = "You approach the door of the house.\nYou are about to knock when the door opens and out steps a x##100.\nEep! This is the x##100's house!\nYou feel a bit under-prepared for this, what with only having a tiny dagger.\nWould you like to (1) fight or (2) run away? "
        enter_w_sword = "You approach the door of the house.\nYou are about to knock when the door opens and out steps a x##100.\nEep! This is the x##100's house!\nThe x##100 attacks you!\nWould you like to (1) fight or (2) run away?"
        enter_cave = "You peer cautiously into the cave.\nIt turns out to be only a very small cave.\nYour eye catches a glint of metal behind a rock.\nYou have found the magical Sword of Ogorth!\nYou discard your silly old dagger and take the sword with you.\nYou walk back out to the field.\n"
        enter_cave_again = "You peer cautiously into the cave.\nYou've been here before, and gotten all the good stuff. It's just an empty cave now.\nYou walk back out to the field.\n"
        fight_sword = "As the x##100 moves to attack , you unsheathe your new sword.\nThe sword of Ogorth shines brightly in your hand as you brace yourself for the attack.\nBut the x##100 takes one look at your shiny new toy and runs away!\nYou have rid the town of the x##100. You are victorious!\nWould you like to play again? (y/n)"
        run = "You run back into the field. Luckily you don't seem to have been followed.\n"
        lose_game = "You do your best..\nbut your dagger is no match for the x##100.\nYou have been defeated!\nWould you like to play again? (y/n)"
        decide = "Enter 1 to knock on the door of the house.\nEnter 2 to peer into the cave.\nwhat would you like to do?\n(please enter 1 or 2)"

        names = ['gremlin', 'witch', 'wicked sherman', 'dragon', 'troll','serpent','werewolf','vampire','kraken','cyclops','gorgon','basilisk','sphinx','Minotaur', 'Hydrahead']
        # Function to replace placeholders with a random name
        def replace_placeholder(sentence, name):
            return sentence.replace("x##100", name)

        # Randomly select a name from the list
        random_name = random.choice(names)

        # Replace placeholders in sentences with the random name
        start = replace_placeholder(start, random_name)
        enter_no_sword = replace_placeholder(enter_no_sword, random_name)
        enter_w_sword = replace_placeholder(enter_w_sword, random_name)
        enter_cave = replace_placeholder(enter_cave, random_name)
        enter_cave_again = replace_placeholder(enter_cave_again, random_name)
        fight_sword = replace_placeholder(fight_sword, random_name)
        lose_game = replace_placeholder(lose_game, random_name)


        sword = 0
        loop = True # Loop is for running the while loop continuously
        print_sentences(start)
        

        while loop == True:

            print_sentences(decide)

            # User would like to go in house or in cave?
            user_glb= user_input()

            #1. Part 1

            #user goes in the house with no sword
            if user_glb == 1 and sword == 0:
                print_sentences(enter_no_sword)
                user= user_input()

                #user chooses to fight
                if user == 1:
                    print_sentences(lose_game) #user 
                    #ask user if he would like to play again and start game allover again if the user picks y instad of n
                    user = end_or_not()
                    if user == "y":
                        sword = 0
                        loop = False
                        #This is where I will update the Random Stuff to change the name of the creature
                    elif user == "n":
                        sword = 0
                        loop = False
                        globe = False

                # User chooses to run
                elif user == 2:
                    print_sentences(run)
                

            #2. Part 2

            # User goes in the house with sword
            elif user_glb== 1 and sword == 1:
                print_sentences(enter_w_sword)

                #User chooses to fight
                #user= int(input('here:'))
                user= user_input()
                if user == 1:
                    print_sentences(fight_sword)# user wins
                    #ask user if he would like to play again and start game allover again if the user picks y instad of n
                    #user = input('here:')
                    user = end_or_not()
                    if user == "y":
                        sword = 0
                        loop = False
                        #This is where I will update the Random Stuff
                    elif user == "n":
                        sword = 0
                        loop = False
                        globe = False
    
                #user runs
                elif user == 2:
                    print_sentences(run)
                    #user returns to the door and cave decision again
                

            # Cave Story

            #User chooses to enter cave no sword
            elif user_glb == 2 and sword== 0:
                print_sentences(enter_cave)
                sword = 1 #user picks sword
            #user enters cave despite having sword
            elif user_glb == 2 and sword == 1:
                print_sentences(enter_cave_again)
           
game()


#print_sentences(open_files("RunDontFight.txt"))

#print("helloe")