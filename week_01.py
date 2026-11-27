print("Hello Periode 2!")



player_name = input("What is your name? Younes")
 
player_gold = 100

inventory = []
 
print("Welcome to the Fantasy Item Shop!")

print(f"Hello {player 1}! You have {100} gold.")
 
items = ["Sword", "Shield", "Potion", "Bow"]
 
print("\nItems for sale:")
 
for item in items:

    print(item)
 
while True:

    print("\n=== Fantasy Item Shop ===")

    print("1. Buy Sword (50 gold)")

    print("2. Buy Shield (40 gold)")

    print("3. Buy Potion (20 gold)")

    print("4. Buy Bow (60 gold)")

    print("5. View Inventory")

    print("6. Exit Shop")
 
    choice = input("What would you like to do? ")
 
    match choice:

        case "1":

            if player_gold >= 50:

                player_gold -= 50

                inventory.append("Sword")

                print("You bought a Sword!")

                print(f"Remaining gold: {player_gold}")

            else:

                print("You don't have enough gold!")
 
        case "2":

            if player_gold >= 40:

                player_gold -= 40

                inventory.append("Shield")

                print("You bought a Shield!")

                print(f"Remaining gold: {player_gold}")

            else:

                print("You don't have enough gold!")
 
        case "3":

            if player_gold >= 20:

                player_gold -= 20

                inventory.append("Potion")

                print("You bought a Potion!")

                print(f"Remaining gold: {player_gold}")

            else:

                print("You don't have enough gold!")
 
        case "4":

            if player_gold >= 60:

                player_gold -= 60

                inventory.append("Bow")

                print("You bought a Bow!")

                print(f"Remaining gold: {player_gold}")

            else:

                print("You don't have enough gold!")
 
        case "5":

            if len(inventory) == 0:

                print("Your inventory is empty!")

            else:

                print("Your inventory:")

                for item in inventory:

                    print("-", item)
 
        case "6":

            print(f"Thanks for visiting, {player_name}!")

            print(f"You have {player_gold} gold left.")

            break
 
        case _:

            print("Invalid choice! Try again.")

 