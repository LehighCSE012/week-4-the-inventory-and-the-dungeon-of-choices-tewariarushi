#Arushi Tewari
#Week 4 Coding Assignment

import random

#Inventory System
inventory = []
def acquire_item(inventory, item):
    inventory.append(item)
    print(f"You aquired a {item}")
    return inventory
def display_inventory(inventory):
    if (inventory == []):
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")
def aquire_item(inventory, item):
    if item is not None:
        inventory.append(item)
        print(f"You aquire the {item}")
        return inventory
def enter_dungeon(player_health, inventory, dungeon_rooms):
    for room in dungeon_rooms:
        room_description, item, challenge_type, challenge_outcome = room

        # Print room description
        print(f"\n{room_description}")

        inventory = aquire_item(inventory, item)
        
        # Handle challenge types
        if challenge_type == "puzzle":
            print("You encounter a puzzle!")
            player_choice = input("Do you want to 'solve' or 'skip' the puzzle? ").strip().lower()
            if player_choice == "solve":
                success = random.choice([True, False])
                if success:
                    print(challenge_outcome[0])  # Success message
                    player_health += challenge_outcome[2]  # Health change
                else:
                    print(challenge_outcome[1])  # Failure message
                    player_health += challenge_outcome[2]  # Health change
        elif challenge_type == "trap":
            print("You see a potential trap!")
            player_choice = input("Do you want to 'disarm' or 'bypass' the trap? ").strip().lower()
            if player_choice == "disarm":
                success = random.choice([True, False])
                if success:
                    print(challenge_outcome[0])  # Success message
                    player_health += challenge_outcome[2]  # Health change
                else:
                    print(challenge_outcome[1])  # Failure message
                    player_health += challenge_outcome[2]  # Health change
        elif challenge_type == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")
        
        # Update player health if it drops below 0
        if player_health < 0:
            player_health = 0
            print("You are barely alive!")

        # Display updated inventory after each room
        display_inventory(inventory)

    # After exiting the dungeon, display player health
    print(f"\nYour final health is {player_health}.")

    return player_health, inventory# Your code goes here
