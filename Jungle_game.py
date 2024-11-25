import random

def start_game():
    print("🌴 Welcome to Jungle Adventure! 🌴")
    print("You're lost in a dense jungle. Your goal is to find the hidden treasure and escape.")
    print("Beware of wild animals and other dangers!\n")
    main_menu()

def main_menu():
    print("What would you like to do?")
    print("1. Explore the jungle")
    print("2. Check inventory")
    print("3. Quit the game")
    choice = input("> ")
    
    if choice == "1":
        explore_jungle()
    elif choice == "2":
        check_inventory()
    elif choice == "3":
        print("Thanks for playing Jungle Adventure!")
        exit()
    else:
        print("Invalid choice. Try again.")
        main_menu()

inventory = []
health = 100

def explore_jungle():
    global health
    events = [
        "You found a banana tree and ate some fruit. (+10 health)",
        "A wild tiger appeared! You barely escaped. (-20 health)",
        "You discovered a hidden treasure chest! (Treasure added to inventory)",
        "You stumbled into a snake pit! (-30 health)",
        "You found a stream and drank water. (+10 health)",
    ]
    event = random.choice(events)
    print("\n" + event)
    
    if "banana tree" in event or "stream" in event:
        health += 10
    elif "tiger" in event or "snake pit" in event:
        health -= 20 if "tiger" in event else 30
    elif "treasure chest" in event:
        inventory.append("Treasure")
    
    print(f"Health: {health}")
    if health <= 0:
        print("You have succumbed to the dangers of the jungle. Game over!")
        exit()
    
    main_menu()

def check_inventory():
    print("\nInventory:")
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")
    print(f"Health: {health}")
    print("")
    main_menu()

# Start the game
start_game()
