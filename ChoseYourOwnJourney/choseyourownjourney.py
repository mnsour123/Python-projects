import random

name = input("What is your name: ")
print("Welcome", name, "to this journey!")

inventory = []
health = 100

def show_status():
    print(f"Health: {health} | Inventory: {inventory}")

answer = input(
    "You stumble upon a lonely road. The wind is cold, and the sky is turning dark.\n"
    "Suddenly, you reach a dead end.\n"
    "Do you want to (A) climb the wall or (B) look for a hidden path? "
).lower()

if answer == "a":
    print("You place your hands on the rough stones and climb. Halfway up, the wall begins to shake...")
    choice = input("Do you (A) jump down or (B) keep climbing? ").lower()

    if choice == "a":
        print("You jump down safely, but a mysterious hooded figure appears.")
        print("The figure hands you a small glowing key.")
        inventory.append("glowing key")

    elif choice == "b":
        print("You reach the top and discover an abandoned tower.")
        print("Inside, you find a rusty sword.")
        inventory.append("rusty sword")

        # New branch: explore the tower further
        explore = input("Do you want to (A) explore the tower further or (B) climb back down? ").lower()
        if explore == "a":
            print("Deep inside, you find a dusty chest with a shield inside!")
            inventory.append("shield")
        else:
            print("You climb back down, sword in hand.")

    else:
        print("Invalid choice, the journey fades away...")

elif answer == "b":
    print("You brush aside the bushes and discover a narrow hidden trail leading underground.")
    choice = input("Do you (A) enter the tunnel or (B) stay outside? ").lower()

    if choice == "a":
        print("Inside the tunnel, ancient carvings whisper your name...")
        print("You find an old map and take it with you.")
        inventory.append("old map")

        # New branch: follow the map
        follow = input("Do you want to (A) follow the map deeper or (B) turn back? ").lower()
        if follow == "a":
            print("The map leads you to a hidden stash of gold coins!")
            inventory.append("gold coins")
        else:
            print("You decide it's too risky and turn back.")

    elif choice == "b":
        print("You stay outside, but the ground begins to rumble...")
        print("A small pouch falls from the sky. Inside is a healing potion.")
        inventory.append("healing potion")

    else:
        print("Invalid choice, the journey fades away...")

else:
    print("You stand still, unsure. The world around you slowly disappears...")

show_status()
print("\nAs you continue your journey...")

enemy = random.choice(["a wild wolf", "a bandit", "a shadow creature"])
print("Suddenly, you are confronted by", enemy + "!")

fight = input("Do you want to (A) fight or (B) run? ").lower()

if fight == "a":
    if "rusty sword" in inventory and "shield" in inventory:
        print("With sword and shield, you easily defeat the enemy!")
    elif "rusty sword" in inventory:
        print("You swing your rusty sword and defeat the enemy!")
    elif "glowing key" in inventory:
        print("The glowing key flashes and blinds the enemy, letting you slip away unharmed!")
    else:
        print("You try to fight with your bare hands but the enemy is too strong.")
        health -= 40
        if "healing potion" in inventory:
            print("Luckily, you drink your healing potion and recover some strength.")
            inventory.remove("healing potion")
            health += 20
        print("You barely escape with your life.")

elif fight == "b":
    print("You run as fast as you can and manage to escape.")

else:
    print("Frozen by fear, you do nothing. The enemy disappears into the shadows.")

print("\n--- The End ---")
show_status()

if health <= 0:
    print("Your journey ends here...")
elif "gold coins" in inventory:
    print(f"{name}, you emerge from the journey rich and victorious!")
else:
    print(f"{name}, your journey continues another day...")
