import random

import sys
import time

def write(*args):
    for arg in args:
        for char in arg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.002)

def flagArt():
    write("""
VVVVVVVVV  XXX  VVVVVVVVVVVVVVVVVV      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
VVVVVVVVV  XXX  VVVVVVVVVVVVVVVVVV      X..............XXXX..............X
VVVVVVVVV  XXX  VVVVVVVVVVVVVVVVVV      X..............XXXX..............X
___________XXX____________________      X..............XXXX..............X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
_________  XXX  __________________      X..............XXXX..............X
VVVVVVVVV  XXX  VVVVVVVVVVVVVVVVVV      X..............XXXX..............X
VVVVVVVVV  XXX  VVVVVVVVVVVVVVVVVV      X..............XXXX..............X
VVVVVVVVV  XXX  VVVVVVVVVVVVVVVVVV      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
""")

flagArt()

def main():
    write("THE GREAT VIKING WAR   ")
    write("The year is 984 and the kingdom of England and the kingdom of Norway are in a MASSIVE war against each other.  ")
    write("During a raid from Norway, they managed to get their hands on a lot of precious war resources, including prisoners.  ")
    write("Many people were captured and taken into custody in a giant prison on the coast of Norway.  ")
    write("During your stay, you see a chance to escape. You grab a brick laying on the floor and throw it at the window.  ")
    write("You slip through the small window, fall down, and land on the top of a large viking ship. ")
    write("You swiftly retract the anchor and set sail.  ")
    write("You must make your way all across the North Sea to make it back to England.  ")
    write("However, the vikings want their ship back and are chasing you across the sea!  ")
    write("You have 1 canteen and a fighting spirit.  ")
    write("Survive the rough waters of the ocean and outrun the vikings! Home is 200 miles away. Get there and you win! Good luck!\n")

    miles_traveled = 0
    thirst = 0
    shiphealth = 0
    vikings_distance = -20
    canteen = 3
    done = False

    while not done:
        print("\nA. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("F. Roll a magical 100 sided viking dice. (May have side effects such as dying)")
        print("Q. Quit.")
        user_choice = input("What will you do? ").upper()

        if user_choice == "Q":
            print("You quit the game. Why would you even do that? The vikings caught you by the way.")
            done = True

        elif user_choice == "E":
            print(f"\nMiles traveled: {miles_traveled}")
            print(f"Drinks in canteen: {canteen}")
            print(f"Your ship's health: {shiphealth}")
            print(f"The vikings are {miles_traveled - vikings_distance} miles behind you.")

        elif user_choice == "A":
            if canteen > 0:
                canteen -= 1
                thirst = 0
                print("You take a drink.")
            else:
                print("Your canteen is empty!")

        elif user_choice == "B":
            miles = random.randint(5, 12)
            miles_traveled += miles
            thirst += 1
            shiphealth -= 1
            vikings_distance += random.randint(7, 14)
            print(f"You moved ahead {miles} miles at moderate speed.")

        elif user_choice == "C":
            miles = random.randint(10, 20)
            miles_traveled += miles
            thirst += 1
            tired = random.randint(1, 3)
            shiphealth -= tired
            vikings_distance += random.randint(7, 14)
            print(f"You moved ahead {miles} miles at full speed. Your ship got {tired} health.")

        elif user_choice == "D":
            shiphealth = 0
            print("You stopped for the night. Your ship is in good condition.")
            vikings_distance += random.randint(7, 14)

        elif user_choice == "F":
            roll = random.randint(1,100)
            print(f"You rolled a {roll} on the magical 100 sided viking dice.")
            if roll == 100:
                print("You rolled the highest number, a 100, it must be a good sign. All of the sudden a British ship picks you up and sends you back to your home. You win!")
                done = True
            else:
                print("You rolled less than 100, YOU LOSE!")
                done = True

        # Random iceberg event
        if not done and random.randint(1, 20) == 10:
            print("\nYou found a lone traveler on the coast of a remote island. He offers you assistance on your broken down ship as well as a full bottle of water. You thank him and continue on your journey.")
            canteen = 3
            thirst = 0
            shiphealth = 7

        # Status warnings
        if thirst > 4 and thirst <= 6 and not done:
            print("You are thirsty.")
        if shiphealth > 5 and shiphealth <= 8 and not done:
            print("Your ship is getting beaten up.")
        if miles_traveled - vikings_distance < 15 and not done:
            print("The vikings are getting close!")

        # Game over
        if thirst > 6:
            print("You died of thirst!")
            print("The vikings saw this and took account of it. They will bring extra water on their next raid. Thanks for playing!")
            done = True
        elif shiphealth > 8:
            print("Your ship has sunk.")
            print("The vikings have found your shipwreck and looted your body. Thanks for playing!")
            done = True
        elif vikings_distance >= miles_traveled:
            print("The vikings speared you down!")
            print("They stole your ship and looted your body. Thanks for playing!")
            done = True
        elif miles_traveled >= 200:
            print("You won! You crossed the ocean and escaped the vikings. Thanks for playing!")
            done = True

if __name__ == "__main__":
    main()